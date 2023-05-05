from collections import deque

n = int(input())
g = [[] for _ in range(n + 1)]
v = [False] * (n + 1)
dic = {}
for i in range(1, n+1):
    a = list(map(int, input().split()))
    dic[i] = a[0]
    g[i] = a[2:]

dp = [-1] * (n + 1)

def go(idx):
    if dp[idx] != -1:
        return dp[idx]

    if not g[idx]:
        dp[idx] = dic[idx]
        return dp[idx]

    tmp = 0
    for next_ in g[idx]:
        tmp = max(tmp, go(next_))
    tmp += dic[idx]

    dp[idx] = tmp
    return dp[idx]

for i in range(1, n + 1):
    go(i)

print(max(dp))
