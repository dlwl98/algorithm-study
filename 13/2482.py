n = int(input())
k = int(input())

if k == 1:
    print(n)
    exit()

dp = [[[0] * 4 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(3, n + 1):
    dp[i][1][0] = i - 2
    dp[i][1][1] = 1
    dp[i][1][2] = 1
    dp[i][2][3] = 1

for i in range(4, n + 1):
    for j in range(2, k + 1):
        dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
        dp[i][j][1] = dp[i-1][j-1][0]
        dp[i][j][2] = dp[i-1][j][2] + dp[i-1][j][3]
        dp[i][j][3] = dp[i-1][j-1][2]
        dp[i][j][0] %= 1000000003
        dp[i][j][1] %= 1000000003
        dp[i][j][2] %= 1000000003
        dp[i][j][3] %= 1000000003

print((dp[n][k][0] + dp[n][k][1] + dp[n][k][2]) % 1000000003)
