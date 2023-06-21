import sys
import heapq
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dp = [[0, 1] for _ in range(n+1)]
v = [False] * (n+1)

def dfs(cur):
    for nxt in g[cur]:
        if not v[nxt]:
            v[nxt] = True
            dfs(nxt)
            dp[cur][0] += dp[nxt][1]
            dp[cur][1] += min(dp[nxt])

v[1] = True
dfs(1)
print(min(dp[1]))
