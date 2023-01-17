from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
w = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
visited = [[[int(1e9)] * 2 for _ in range(M)] for _ in range(N)]
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def bfs():
    visited[0][0][0] = 1
    visited[0][0][1] = 1
    q = deque([[0, 0, 1]])
    while q:
        y, x, drill = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx][drill] == int(1e9):
                if w[ny][nx] == 1 and drill > 0:
                    visited[ny][nx][0] = visited[y][x][drill] + 1
                    q.append([ny, nx, 0])
                if w[ny][nx] == 0:
                    visited[ny][nx][drill] = visited[y][x][drill] + 1
                    q.append([ny, nx, drill])


def solution():
    bfs()
    result = min(visited[-1][-1])
    print(-1 if result == int(1e9) else result)


solution()
