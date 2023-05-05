from sys import stdin
import sys
sys.setrecursionlimit(10**5)

def solution():
    n, m, k = map(int, stdin.readline().split())
    g = [[-1] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, h = map(int, stdin.readline().split())
        g[a][b] = h
        g[b][a] = h

    dp = [[-1] * (k + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)

    def dfs(s, r):
        if dp[s][r] != -1:
            return dp[s][r]

        if g[s][n] != -1:
            if r == 0:
                dp[s][r] = g[s][n]
                return g[s][n]
            else:
                dp[s][r] = 0
                return 0

        tmp = 10**9
        for i in range(1, n + 1):
            if g[s][i] == -1 or visited[i]:
                continue

            visited[i] = True
            tmp = min(tmp, g[s][i] + dfs(i, r))
            if r > 0:
                tmp = min(tmp, dfs(i, r-1))
            visited[i] = False

        dp[s][r] = tmp
        return tmp

    visited[1] = True
    dfs(1, k)
    print(dp[1][k])

solution()
