import sys
input = sys.stdin.readline

n, t = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (t+1)
for k, s in g:
    dp2 = [0] * (t+1)
    for i in range(t+1):
        dp2[i] = dp[i]
    for i in range(t+1):
        if (i + k <= t):
            dp2[i + k] = max(dp[i + k], dp[i] + s)
    for i in range(t+1):
        dp[i] = dp2[i]
print(max(dp))
