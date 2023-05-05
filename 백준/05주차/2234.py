from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
G = [list(map(int, stdin.readline().split())) for _ in range(N)]
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
flag = (2, 8, 1, 4)


def bfs(sy, sx, visited, tmp):
    visited[sy][sx][0] = 1
    q_tmp = deque([[sy, sx]])
    q = deque([[sy, sx]])
    cnt = 0
    while q:
        y, x = q.popleft()
        cnt += 1
        for i in range(4):
            if flag[i] & G[y][x]:
                continue
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx][0]:
                visited[ny][nx][0] = 1
                q.append([ny, nx])
                q_tmp.append([ny, nx])

    while q_tmp:
        y, x = q_tmp.popleft()
        visited[y][x][0] = cnt
        visited[y][x][1] = tmp


def solution():
    cnt = 0
    max_ = 0
    result = 0
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j][0]:
                cnt += 1
                bfs(i, j, visited, cnt)

    print(cnt)

    for i in range(N):
        for j in range(M):
            max_ = max(max_, visited[i][j][0])
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if 0 <= ny < N and 0 <= nx < M and visited[i][j][1] != visited[ny][nx][1]:
                    result = max(result, visited[i][j][0] + visited[ny][nx][0])
    print(max_)
    print(result)


solution()
