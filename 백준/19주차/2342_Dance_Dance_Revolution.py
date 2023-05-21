import sys
input = sys.stdin.readline

def get_add(a, b):
    if a == 0:
        return 2
    if a == b:
        return 1
    if abs(a - b) == 2:
        return 4
    else:
        return 3


g = list(map(int, input().split()))
g.pop()
n = len(g)
if n == 0:
    print(0)
    exit()

dp = [[[10**9] * 5 for _ in range(5)] for _ in range(n + 1)]
dp[-1][0][0] = 0

for i in range(n):
    for r in range(5):
        for k in range(5):
            add = get_add(k, g[i])
            dp[i][g[i]][r] = min(dp[i][g[i]][r], dp[i - 1][k][r] + add)

    for l in range(5):
        for k in range(5):
            add = get_add(k, g[i])
            dp[i][l][g[i]] = min(dp[i][l][g[i]], dp[i - 1][l][k] + add)

result = 10**9
for l in range(5):
    for r in range(5):
        result = min(result, dp[n - 1][l][r])
print(result)
