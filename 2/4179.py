from sys import stdin
from collections import deque

R, C = map(int, stdin.readline().split())
g = [list(stdin.readline().rstrip()) for _ in range(R)]
dy, dx = (0, 0, -1, 1), (-1, 1, 0, 0)
jh = [0, 0]
f = []
for i in range(R):
    for j in range(C):
        if g[i][j] == 'J':
            jh = [i, j]
        if g[i][j] == 'F':
            f.append((i, j))


def fire():
    global f
    visited = [[False] * C for _ in range(R)]
    tmp = []
    for y, x in f:
        visited[y][x] = True
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny < 0 or nx < 0 or ny >= R or nx >= C or visited[ny][nx]:
                continue
            if g[ny][nx] == '.' or g[ny][nx] == 'J':
                g[ny][nx] = 'F'
                visited[ny][nx] = True
                tmp.append((ny, nx))
    f = tmp


def bfs():
    r, c = jh
    visited = [[False] * C for _ in range(R)]
    visited[r][c] = True
    prev_tick = 1
    queue = deque([[r, c, prev_tick]])
    while queue:
        y, x, tick = queue.popleft()
        if tick > prev_tick:
            prev_tick = tick
            fire()
        if g[y][x] == 'F':
            continue
        if y == 0 or y == R - 1 or x == 0 or x == C - 1:
            return tick
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny < 0 or nx < 0 or ny >= R or nx >= C or visited[ny][nx]:
                continue
            if g[ny][nx] == '.':
                queue.append([ny, nx, tick + 1])
                visited[ny][nx] = True
    return -1


def solution():
    result = bfs()
    if result == -1:
        print("IMPOSSIBLE")
    else:
        print(result)


solution()
