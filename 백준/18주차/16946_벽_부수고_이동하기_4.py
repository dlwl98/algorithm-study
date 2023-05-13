import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input().rstrip())) for _ in range(n)]
v = [[0] * m for _ in range(n)]
parent = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        parent[i][j] = (i, j)

def inRange(y, x):
    return 0 <= y < n and 0 <= x < m

for i in range(n):
    for j in range(m):
        if v[i][j] or g[i][j]:
            continue
        q = deque()
        q.append((i, j))
        tmp = [(i, j)]
        v[i][j] = 1
        while q:
            y, x = q.popleft()
            for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if inRange(ny, nx) and not v[ny][nx] and not g[ny][nx]:
                    v[ny][nx] = 1
                    tmp.append((ny, nx))
                    q.append((ny, nx))
        acc = len(tmp)
        for y, x in tmp:
            parent[y][x] = (i, j)
        v[i][j] = acc
        
for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            print(0, end='')
            continue

        tmp = set()
        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny, nx = i + dy, j + dx
            if inRange(ny, nx) and v[ny][nx]:
                tmp.add(parent[ny][nx])

        acc = 1
        for y, x in tmp:
            acc += v[y][x]
        print(acc % 10, end='')
    print()

