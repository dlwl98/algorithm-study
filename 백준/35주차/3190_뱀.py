import sys
from collections import deque
input = sys.stdin.readline

def mapfuc(c):
    return int(c) - 1

n = int(input())
k = int(input())
appleSet = set([tuple(map(mapfuc, input().split())) for _ in range(k)])
l = int(input())
tmp = []
for _ in range(l):
    a, b = input().rstrip().split()
    tmp.append([int(a), -1 if b == 'L' else 1])
changes = [0] * 10001
for a, b in tmp:
    changes[a] = b
d = ((-1, 0), (0, 1), (1, 0), (0, -1))

def inRange(y, x):
    return 0 <= y < n and 0 <= x < n

snakeSet = set([(0, 0)])
snake = deque([[0, 0]])
direction = 1
tick = 0
while True:
    tick += 1
    hy, hx = snake[-1]
    ny = hy + d[direction][0]
    nx = hx + d[direction][1]
    direction = (direction + changes[tick]) % 4

    if not inRange(ny, nx):
        print(tick)
        exit()
    if (ny, nx) in snakeSet:
        print(tick)
        exit()
    
    snake.append([ny, nx])
    snakeSet.add((ny, nx))
    if (ny, nx) not in appleSet:
        ty, tx = snake.popleft()
        snakeSet.remove((ty, tx))
    else:
        appleSet.remove((ny, nx))
