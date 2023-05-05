from collections import deque
from itertools import combinations

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
groups = []


def bfs(y, x, visited):
    groups.append([[y, x]])
    visited[y][x] = True
    q = deque([[y, x]])

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and G[ny][nx] == 2:
                visited[ny][nx] = True
                groups[-1].append([ny, nx])
                q.append([ny, nx])


def check():
    cnt = 0
    for group in groups:
        flag = False
        for y, x in group:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    continue
                if G[ny][nx] == 0:
                    flag = True
        cnt += 0 if flag else len(group)
    return cnt


def solution():
    empty = []
    tmp = []
    cnt = 0
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if G[i][j] == 0:
                empty.append([i, j])
                tmp.append(cnt)
                cnt += 1
            if not visited[i][j] and G[i][j] == 2:
                bfs(i, j, visited)

    result = 0
    combs = combinations(tmp, 2)
    for a, b in combs:
        ay, ax = empty[a]
        by, bx = empty[b]
        G[ay][ax] = 1
        G[by][bx] = 1
        result = max(result, check())
        G[ay][ax] = 0
        G[by][bx] = 0

    print(result)


solution()
