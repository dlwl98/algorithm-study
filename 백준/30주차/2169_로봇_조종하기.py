import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

di = ((-1, 0), (0, -1), (0, 1))
n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
dp = [[[None] * 3 for _ in range(m)] for _ in range(n)]
dp[0][0][0] = g[0][0]
dp[0][0][1] = g[0][0]

def inRange(y, x):
    return 0 <= y < n and 0 <= x < m

def go(y, x, d):
    if dp[y][x][d] != None:
        return dp[y][x][d]

    tmp = -10**9
    if d == 0:
        for i in range(3):
            dy, dx = di[i]
            py = y + dy
            px = x + dx
            if inRange(py, px):
                tmp = max(tmp, go(py, px, i) + g[y][x])

    else:
        dy, dx = di[0]
        py = y + dy
        px = x + dx
        if inRange(py, px):
            tmp = max(tmp, go(py, px, 0) + g[y][x])

        dy, dx = di[d]
        py = y + dy
        px = x + dx
        if inRange(py, px):
            tmp = max(tmp, go(py, px, d) + g[y][x])
    
    dp[y][x][d] = tmp
    return tmp

print(go(n-1, m-1, 0))
