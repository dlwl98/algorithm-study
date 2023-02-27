N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

# dfs 풀이

# def dfs(y, x, flag):
#     global cnt
#     if y == N - 1 and x == N - 1:
#         cnt += 1
#         return
#     if y + 1 < N and x + 1 < N:
#         if G[y + 1][x + 1] == 0 and G[y][x + 1] == 0 and G[y + 1][x] == 0:
#             dfs(y + 1, x + 1, 1)
#
#     if flag == 0 or flag == 1:
#         if x + 1 < N:
#             if G[y][x + 1] == 0:
#                 dfs(y, x + 1, 0)
#
#     if flag == 1 or flag == 2:
#         if y + 1 < N:
#             if G[y + 1][x] == 0:
#                 dfs(y + 1, x, 2)
#
#
# def solution():
#     dfs(0, 1, 0)
#     print(cnt)
#
#
# solution()

# dp 풀이

dp = [[[0] * N for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1

for i in range(2, N):
    if G[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for r in range(1, N):
    for c in range(1, N):
        if G[r][c] == 0 and G[r][c - 1] == 0 and G[r - 1][c] == 0:
            dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

        if G[r][c] == 0:
            dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
            dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]

print(sum(dp[i][N - 1][N - 1] for i in range(3)))
