# 다익스트라 시간초과풀이
# import heapq

# n = int(input())
# g = [list(map(int, input().split())) for _ in range(n)]

# q = []
# heapq.heappush(q, [g[0][0] + g[1][1], 0, 1, 2])
# heapq.heappush(q, [g[0][0] + g[1][2], 0, 2, 2])
# heapq.heappush(q, [g[0][1] + g[1][0], 1, 0, 2])
# heapq.heappush(q, [g[0][1] + g[1][2], 1, 2, 2])
# heapq.heappush(q, [g[0][2] + g[1][0], 2, 0, 2])
# heapq.heappush(q, [g[0][2] + g[1][1], 2, 1, 2])
# while q:
#     acc, start, before, cnt = heapq.heappop(q)
#     if cnt == n:
#         print(acc)
#         break
#     for i in range(3):
#         if i == before: 
#             continue
#         if cnt == n-1 and i == start: 
#             continue
#         heapq.heappush(qq, [acc + g[cnt][i], start, i, cnt+1])

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
dp = [[[10**9] * 3 for _ in range(3)] for _ in range(n+1)]

dp[2][0][1] = g[0][0] + g[1][1]
dp[2][0][2] = g[0][0] + g[1][2]
dp[2][1][0] = g[0][1] + g[1][0]
dp[2][1][2] = g[0][1] + g[1][2]
dp[2][2][0] = g[0][2] + g[1][0]
dp[2][2][1] = g[0][2] + g[1][1]

for i in range(3, n+1):
    for j in range(3):
        for k in range(3):
            if k == 0:
                dp[i][j][k] = min(dp[i][j][k], g[i-1][0] + dp[i-1][j][1], g[i-1][0] + dp[i-1][j][2])
            elif k == 1:
                dp[i][j][k] = min(dp[i][j][k], g[i-1][1] + dp[i-1][j][0], g[i-1][1] + dp[i-1][j][2])
            elif k == 2:
                dp[i][j][k] = min(dp[i][j][k], g[i-1][2] + dp[i-1][j][0], g[i-1][2] + dp[i-1][j][1])

result = 10**9
for i in range(3):
    for j in range(3):
        if i == j: 
            continue
        result = min(result, dp[n][i][j])

print(result)
