n, k = map(int, input().split())
v = [0]
w = [0]
for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)


def solution():
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j < w[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i]] + v[i])

    print(dp[n][k])


solution()
