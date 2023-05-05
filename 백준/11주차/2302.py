n = int(input())
m = int(input())
g = []
tmp = 0
for _ in range(m):
    i = int(input())
    g.append(i - tmp - 1)
    tmp = i
if tmp < n:
    g.append(n - tmp)

dp = [[0, 0] for _ in range(n + 1)]
dp[0] = [1, 0]
dp[1] = [1, 0]

for i in range(2, n + 1):
    dp[i] = [dp[i-1][0] + dp[i-1][1], dp[i-1][0]]

result = 1
for i in g:
    result *= dp[i][0] + dp[i][1]
print(result)
