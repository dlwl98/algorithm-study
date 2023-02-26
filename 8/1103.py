from collections import deque


def go():
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)
    q = deque()
    q.append([0, 0])
    result = 1
    while q:
        y, x = q.popleft()
        result = dp[y][x]
        if result > n * m:
            return -1
        for i in range(4):
            ny = y + dy[i] * int(g[y][x])
            nx = x + dx[i] * int(g[y][x])
            if 0 <= ny < n and 0 <= nx < m and g[ny][nx] != 'H':
                if dp[ny][nx] < dp[y][x] + 1:
                    dp[ny][nx] = dp[y][x] + 1
                    q.append([ny, nx])

    return result


def solution():
    global n, m, g, dp
    n, m = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    dp = [[-1] * m for _ in range(n)]
    dp[0][0] = 1

    print(go())


solution()
