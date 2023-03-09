from sys import stdin

def solution():
    n = int(stdin.readline())
    g = [list(map(int, stdin.readline().split())) for _ in range(n)]
    dp = [[-1] * n for _ in range(n)]

    def dfs(y, x):
        if dp[y][x] != -1:
            return dp[y][x]

        tmp = 0
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < n and g[y][x] < g[ny][nx]:
                tmp = max(tmp, dfs(ny, nx))

        dp[y][x] = tmp + 1
        return dp[y][x]

    result = 0
    for i in range(n):
        for j in range(n):
            result = max(result, dfs(i, j))

    print(result)

solution()
