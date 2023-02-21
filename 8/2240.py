T, W = map(int, input().split())
G = [int(input()) for _ in range(T)]
dp = [[[0] * 3 for _ in range(W+1)] for _ in range(T+1)]


def toggle(tree):
    if tree == 1:
        return 2
    else:
        return 1


def solution():
    for i in range(1, T+1):
        for j in range(0, W+1):
            for k in range(1, 3):
                if j == 0:
                    if G[i-1] == k and k == 1:
                        dp[i][j][k] = dp[i-1][j][k] + 1
                    continue

                if G[i-1] == k:
                    dp[i][j][k] = max(dp[i-1][j-1][toggle(k)] + 1, dp[i-1][j][k] + 1)
                else:
                    dp[i][j][k] = max(dp[i-1][j-1][toggle(k)], dp[i-1][j][k])

    print(max(max(dp[-1])))


solution()
