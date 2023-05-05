from sys import stdin

def solution():
    n, m = map(int, stdin.readline().split())
    g = [list(map(int, stdin.readline().rstrip('\n'))) for _ in range(n)]
    dp = [[-1] * m for _ in range(n)]

    def dfs(y, x):
        if dp[y][x] != -1:
            return dp[y][x]

        tmp = 10**9
        cnt = 0
        for dy, dx in ((1, 1), (1, 0), (0, 1)):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m and g[ny][nx] == 1:
                cnt += 1
                tmp = min(tmp, dfs(ny, nx))

        if cnt == 3:
            dp[y][x] = tmp + 1
        else:
            dp[y][x] = 1
        return dp[y][x]

    result = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                result = max(result, dfs(i, j))

    print(result ** 2)

solution()
