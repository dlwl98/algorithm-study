import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def inRange(y, x):
    return 0 <= y < n and 0 <= x < m

v = [[[False] * 2 for _ in range(m)] for _ in range(n)]
q = deque()
q.append([0, 0, 1, 1])
v[0][0][1] = True
while q:
    y, x, flag, cnt = q.popleft()
    if (y, x) == (n-1, m-1):
        print(cnt)
        exit()
    for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ny, nx = y + dy, x + dx
        if inRange(ny, nx) and not v[ny][nx][flag]:
            if g[ny][nx] == 1:
                if flag == 1:
                    v[ny][nx][0] = True
                    q.append([ny, nx, 0, cnt+1])
            else:
                v[ny][nx][flag] = True
                q.append([ny, nx, flag, cnt+1])

print(-1)
