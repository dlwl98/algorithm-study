N = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))


def solution():
    dp = [[0] * 100 for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, 100):
            if j < L[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])

    print(dp[N][99])


solution()
