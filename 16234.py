from sys import stdin
from collections import deque


n, L, R = map(int, stdin.readline().split())
g = [list(map(int, stdin.readline().split())) for _ in range(n)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def go(sy, sx, visited):
    cnt = 1
    sum_num = g[sy][sx]
    local_visit = deque([[sy, sx]])
    queue = deque([[sy, sx]])
    visited[sy][sx] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                tmp = abs(g[y][x] - g[ny][nx])
                if not visited[ny][nx] and L <= tmp <= R:
                    cnt += 1
                    sum_num += g[ny][nx]
                    local_visit.append([ny, nx])
                    queue.append([ny, nx])
                    visited[ny][nx] = True

    for i, j in local_visit:
        g[i][j] = sum_num // cnt

    return cnt


def solution():
    cnt = 0
    while True:
        tmp = 0
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    tmp += go(i, j, visited) - 1
        if tmp:
            cnt += 1
        else:
            break

    print(cnt)


solution()

# if __name__ == '__main__':
