import sys
import heapq
from collections import deque
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

def inRange(y, x):
    return 0 <= y < n and 0 <= x < n

def go(num):
    v = [[False] * n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if g[i][j] == num:
                v[i][j] = True
                q.append([i, j, 0])

    while q:
        y, x, dist = q.popleft()
        if g[y][x] != 0 and g[y][x] != num:
            return dist
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = y + dy, x + dx
            if inRange(ny, nx) and not v[ny][nx]:
                v[ny][nx] = True
                q.append([ny, nx, dist + (1 if g[ny][nx] == 0 else 0)])

    return 10**9

cnt = 0
v = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if g[i][j] != 0 and not v[i][j]:
            cnt += 1
            v[i][j] = True
            g[i][j] = cnt
            q = deque([[i, j]])
            while q:
                y, x = q.popleft()
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny, nx = y + dy, x + dx
                    if inRange(ny, nx) and g[ny][nx] != 0 and not v[ny][nx]:
                        g[ny][nx] = cnt
                        v[ny][nx] = True
                        q.append([ny, nx])

result = 10**9
for i in range(1, cnt):
    result = min(result, go(i))

print(result)
