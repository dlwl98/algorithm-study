from collections import deque


n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
result = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            cnt += 1

def inRange(y, x):
    return 0 <= y < n and 0 <= x < m

while cnt > 0:
    result += 1
    v = [[0] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    while q:
        y, x = q.popleft()
        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if not inRange(ny, nx):
                continue
            if g[ny][nx] == 1:
                v[ny][nx] += 1
            elif not v[ny][nx]:
                v[ny][nx] += 1
                q.append((ny, nx))

    disappears = []
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1 and v[i][j] >= 2:
                disappears.append([i, j])

    for y, x in disappears:
        g[y][x] = 0
        cnt -= 1

print(result)
