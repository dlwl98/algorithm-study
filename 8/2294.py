N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [10**9] * 10001


def solution():
    for coin in coins:
        if coin <= 10000:
            dp[coin] = 1

    for i in range(10001):
        for coin in coins:
            if i + coin <= 10000:
                dp[i + coin] = min(dp[i + coin], dp[i] + 1)

    print(dp[K] if dp[K] < 10**9 else -1)


solution()
