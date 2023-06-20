import sys
from collections import deque
input = sys.stdin.readline

d = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))
m, n, h = map(int, input().split())
g = [[[0] * h for _ in range(m)] for _ in range(n)]
for i in range(h):
    for j in range(n):
        arr = list(map(int, input().split()))
        for k in range(m):
            g[j][k][i] = arr[k]

def inRange(y, x, z):
    return 0 <= y < n and 0 <= x < m and 0 <= z < h

result = 0
v = [[[False] * h for _ in range(m)] for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        for k in range(h):
            if g[i][j][k] == 1:
                q.append([0, [i, j, k]])

while q:
    [tick, [y, x, z]] = q.popleft()
    result = max(result, tick)
    for dy, dx, dz in d:
        ny, nx, nz = y + dy, x + dx, z + dz
        if inRange(ny, nx, nz) and g[ny][nx][nz] == 0 and not v[ny][nx][nz]:
            v[ny][nx][nz] = True
            q.append([tick + 1, [ny, nx, nz]])

for i in range(n):
    for j in range(m):
        for k in range(h):
            if g[i][j][k] == 0 and not v[i][j][k]:
                print(-1)
                exit()
print(result)
