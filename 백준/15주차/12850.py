N = 8
dp = {}
D = int(input())

dp[1] = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0],
]

def go(d, start, end):
    if d <= 1:
        return dp[d][start][end]

    if d not in dp:
        dp[d] = [[0 for _ in range(N)] for _ in range(N)]
    if dp[d][start][end]:
        return dp[d][start][end]

    left = d // 2
    right = left + d % 2

    for mid in range(N):
        dp[d][start][end] += go(left, start, mid) * go(right, mid, end)
        dp[d][start][end] %= 1000000007

    return dp[d][start][end]

print(go(D, 0, 0))
