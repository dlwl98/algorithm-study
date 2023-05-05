from collections import deque
from itertools import combinations

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
can_put = []
can_put_idx = []
result = int(1e9)

cnt = 0
zero = 0
for i in range(N):
    for j in range(N):
        if G[i][j] == 2:
            can_put.append((i, j))
            can_put_idx.append(cnt)
            cnt += 1
        if G[i][j] == 0:
            zero += 1


def solution():
    global result
    if zero == 0:
        print(0)
        return

    coms = list(combinations(can_put_idx, M))
    for com in coms:
        tmp = 0
        visited = [[int(1e9)] * N for _ in range(N)]
        queue = deque([])
        for idx in com:
            y, x = can_put[idx]
            queue.append((y, x))
            visited[y][x] = 1
        while queue:
            y, x = queue.popleft()
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0 <= ny < N and 0 <= nx < N and G[ny][nx] != 1 and visited[ny][nx] == int(1e9):
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
                    if G[ny][nx] == 0:
                        tmp += 1
            if tmp == zero:
                result = min(visited[y][x], result)
                break

    print(-1 if result == int(1e9) else result)


solution()
