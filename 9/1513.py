N, M, C = map(int, input().split())
G = [[0] * (M + 1) for _ in range(N + 1)]
for idx in range(1, C + 1):
    y, x = map(int, input().split())
    G[y][x] = idx


def solution():
    dp = [[[[0] * 51 for _ in range(M + 1)] for _ in range(N + 1)] for _ in range(C + 1)]

    flag = 0
    if G[1][1] != 0:
        flag = 1
    dp[flag][1][1][G[1][1]] = 1

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i + j == 2:
                continue
            if G[i][j] == 0:
                dp[flag][i][j][G[1][1]] += dp[flag][i-1][j][G[1][1]] + dp[flag][i][j-1][G[1][1]]

    for c in range(flag + 1, C + 1):
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                for k in range(51):
                    if G[i][j] == 0:
                        dp[c][i][j][k] += dp[c][i - 1][j][k] + dp[c][i][j - 1][k]
                    if G[i][j] != k:
                        if G[i][j] > k:
                            dp[c][i][j][G[i][j]] += dp[c-1][i-1][j][k] + dp[c-1][i][j-1][k]

    for case in dp:
        print(sum(case[N][M]) % 1000007, end=' ')


solution()
