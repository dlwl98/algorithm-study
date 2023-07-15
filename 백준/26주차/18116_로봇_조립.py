import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
robot = [[i, 1] for i in range(10**6 + 1)]

def find(x):
    if robot[x][0] == x:
        return x
    robot[x][0] = find(robot[x][0])
    return robot[x][0]

def union(x, y):
    a = find(x)
    b = find(y)
    if a >= b:
        robot[a][0] = b
        robot[b][1] += robot[a][1]
    else:
        robot[b][0] = a
        robot[a][1] += robot[b][1]

for _ in range(n):
    com = list(input().split())
    if com[0] == 'I':
        t, a, b = com
        a, b = int(a), int(b)
        if(find(a) != find(b)):
            union(a, b)
    elif com[0] == 'Q':
        t, x = com
        print(robot[find(int(x))][1])
