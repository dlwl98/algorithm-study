import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * 3 for _ in range(n)]
    dp[0][0] = g[0][0]
    dp[0][1] = g[1][0]

    for i in range(1, n):
        for j in range(3):
            if j == 0:
                dp[i][j] = g[0][i] + max(dp[i-1][1], dp[i-1][2])
            if j == 1:
                dp[i][j] = g[1][i] + max(dp[i-1][0], dp[i-1][2])
            if j == 2:
                dp[i][j] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])

    print(max(dp[-1]))
