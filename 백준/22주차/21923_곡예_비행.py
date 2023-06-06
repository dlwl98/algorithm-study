import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
up = [[None] * m for _ in range(n)]
down = [[None] * m for _ in range(n)]
up[n-1][0] = g[n-1][0]
down[n-1][m-1] = g[n-1][m-1]

def goup(i, j):
    if up[i][j] != None:
        return up[i][j]
    tmp = max(goup(i+1, j) if i+1 < n else -10**9, goup(i, j-1) if j-1 >= 0 else -10**9)
    up[i][j] = tmp + g[i][j]
    return up[i][j]

def godown(i, j):
    if down[i][j] != None:
        return down[i][j]
    tmp = max(godown(i, j+1) if j+1 < m else -10**9, godown(i+1, j) if i+1 < n else -10**9)
    down[i][j] = tmp + g[i][j]
    return down[i][j]

result = -10**9
for i in range(n):
    for j in range(m):
        result = max(result, goup(i, j) + godown(i, j))
print(result)
