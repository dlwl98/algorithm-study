import heapq
import sys
input = sys.stdin.readline

di = [[-1, 0], [1, 0], [0, 1], [0, -1]]
n = int(input())
g = [list(input().rstrip()) for _ in range(n)]
doors = []
for i in range(n):
    for j in range(n):
        if g[i][j] == '#':
            doors.append([i, j])
sy, sx = doors[0]
ey, ex = doors[1]

def inRange(y, x):
    return 0 <= y < n and 0 <= x < n

dp = [[[10**9] * 4 for _ in range(n)] for _ in range(n)]
pq = []
for i in range(4):
    dp[sy][sx][i] = 0
    heapq.heappush(pq, [0, sy, sx, i])

while pq:
    acc, y, x, before = heapq.heappop(pq)
    if dp[y][x][before] < acc:
        continue
    for i in range(4):
        dy, dx = di[i]
        ny = y + dy
        nx = x + dx
        if not inRange(ny, nx) or g[ny][nx] == '*':
            continue
        if g[y][x] == '!':
            if i == before and dp[ny][nx][i] > acc:
                dp[ny][nx][i] = acc
                heapq.heappush(pq, [acc, ny, nx, i])
            if i != before and dp[ny][nx][i] > acc + 1:
                dp[ny][nx][i] = acc + 1
                heapq.heappush(pq, [acc + 1, ny, nx, i])
        else:
            if i == before or before == None:
                if dp[ny][nx][i] > acc:
                    dp[ny][nx][i] = acc
                    heapq.heappush(pq, [acc, ny, nx, i])

print(min(dp[ey][ex]))
