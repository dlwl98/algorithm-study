import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
dp = [[0, 0] for _ in range(n+1)]
v = [False] * (n+1)

def dfs(start):
    for nxt in g[start]:
        if not v[nxt]:
            v[nxt] = True
            dfs(nxt)
            dp[start][1] += min(dp[nxt][0] , dp[nxt][1])
            dp[start][0] += dp[nxt][1]
    dp[start][1] += 1

if len(g[1]) == 0:
    dp[1][1] = 1
    dp[1][0] = 0
else:
    v[1] = True
    dfs(1)
    
print(min(dp[1][0], dp[1][1]))
