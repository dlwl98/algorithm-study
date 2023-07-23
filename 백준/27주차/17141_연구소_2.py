from collections import deque
from itertools import combinations

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

def inRange(y, x):
    return 0 <= y < n and 0 <= x < n

def bfs(q, cnt):
    v = [[False] * n for _ in range(n)]
    result = 0
    for y, x, t in q:
        v[y][x] = True
    while q:
        y, x, t = q.popleft()
        if t >= cnt:
            return None
        result = max(result, t)
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny = y + dy
            nx = x + dx
            if inRange(ny, nx) and g[ny][nx] != 1 and not v[ny][nx]:
                v[ny][nx] = True
                q.append([ny, nx, t+1])
    for i in range(n):
        for j in range(n):
            if g[i][j] != 1 and v[i][j] == False:
                return None
    return result

possibles = []
for i in range(n):
    for j in range(n):
        if g[i][j] == 2:
            possibles.append([i, j])

result = 10**9
for com in combinations(possibles, m):
    q = deque()
    for y, x in com:
        q.append([y, x, 0])
    bfsResult = bfs(q, result)
    if bfsResult != None:
        result = bfsResult

print(-1 if result == 10**9 else result)
