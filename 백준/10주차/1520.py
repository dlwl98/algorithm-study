import sys
sys.setrecursionlimit(10**6)

def solution():
    n, m = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1] * m for _ in range(n)]

    def dfs(y, x):
        if y == n-1 and x == m-1:
            return 1

        if dp[y][x] != -1:
            return dp[y][x]

        way = 0
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m and g[ny][nx] < g[y][x]:
                way += dfs(ny, nx)

        dp[y][x] = way
        return dp[y][x]

    print(dfs(0, 0))

solution()
