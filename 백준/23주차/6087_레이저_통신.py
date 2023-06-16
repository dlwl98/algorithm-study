import sys
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

w, h = map(int, input().split())
g = [list(input().rstrip()) for _ in range(h)]
c = []
d = ((-1, 0), (0, 1), (1, 0), (0, -1))
for i in range(h):
    for j in range(w):
        if g[i][j] == 'C':
            c.append([i, j])
c1y, c1x = c[0]
c2y, c2x = c[1]

def inRange(y, x):
    return 0 <= y < h and 0 <= x < w

dp = [[[10**9] * 4 for _ in range(w)] for _ in range(h)]
pq = []
heappush(pq, [-1, c1y, c1x, None])
dp[c1y][c1x][0] = -1
dp[c1y][c1x][1] = -1
dp[c1y][c1x][2] = -1
dp[c1y][c1x][3] = -1
while pq:
    acc, y, x, bd = heappop(pq)
    for i in range(4):
        if bd != None and bd % 2 == i % 2 and bd != i:
            continue
        dy, dx = d[i]
        ny = y + dy
        nx = x + dx
        if not inRange(ny, nx) or g[ny][nx] == '*':
            continue
        tmp = acc
        if bd != i:
            tmp += 1
        if dp[ny][nx][i] > tmp:
            dp[ny][nx][i] = tmp
            heappush(pq, [tmp, ny, nx, i])

print(min(dp[c2y][c2x]))
