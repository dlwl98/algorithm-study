from sys import stdin

n = int(stdin.readline())
g = [int(stdin.readline()) for _ in range(n)]

if n <= 2:
    print(sum(g))
elif n == 3:
    print(max(g[0] + g[1], g[0] + g[2], g[1] + g[2]))
else:
    dp = [[0] * 6 for _ in range(n)]
    dp[2][0] = g[1] + g[2]
    dp[2][1] = g[1]
    dp[2][2] = g[0] + g[1]
    dp[2][3] = g[2]
    dp[2][4] = g[0] + g[2]
    dp[2][5] = g[0]

    for i in range(3, n):
        dp[i][0] = max(dp[i-1][3], dp[i-1][4]) + g[i]
        dp[i][1] = max(dp[i-1][3], dp[i-1][4])
        dp[i][2] = dp[i-1][0]
        dp[i][3] = dp[i-1][5] + g[i]
        dp[i][4] = max(dp[i-1][1], dp[i-1][2]) + g[i]
        dp[i][5] = max(dp[i-1][1], dp[i-1][2])

    print(max(dp[-1]))
