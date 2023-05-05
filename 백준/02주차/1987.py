from sys import stdin

R, C = map(int, stdin.readline().split())
g = [list(stdin.readline().rstrip('\n')) for _ in range(R)]
sets = set()
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
result = 0


def dfs(y, x, cnt):
    global result
    result = max(result, cnt)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C:
            if g[ny][nx] not in sets:
                sets.add(g[ny][nx])
                dfs(ny, nx, cnt + 1)
                sets.remove(g[ny][nx])


def solution():
    sets.add(g[0][0])
    dfs(0, 0, 1)
    print(result)


solution()
