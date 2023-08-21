import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
peopleCnt = [0] + list(map(int, input().split()))
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
dp = [[0, 0] for _ in range(n+1)]
v = [False] * (n+1)

def dfs(start):
    for nxt in g[start]:
        if not v[nxt]:
            v[nxt] = True
            dfs(nxt)
            dp[start][1] += dp[nxt][0]
            dp[start][0] += max(dp[nxt])
    dp[start][1] += peopleCnt[start]

v[1] = True
dfs(1)

print(max(dp[1]))
