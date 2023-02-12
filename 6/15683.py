from sys import stdin
from itertools import product

N, M = map(int, stdin.readline().split())
G = [list(map(int, stdin.readline().split())) for _ in range(N)]
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def right(y, x):
    if y == -1 and x == 0:
        return [0, 1]
    elif y == 1 and x == 0:
        return [0, -1]
    elif y == 0 and x == -1:
        return [-1, 0]
    else:
        return [1, 0]


def change(y, x, ddy, ddx, tmp):
    cnt = 0
    while True:
        ny = y + ddy
        nx = x + ddx
        if ny < 0 or nx < 0 or ny >= N or nx >= M or G[ny][nx] == 6:
            break
        if G[ny][nx] == 0:
            tmp.append([ny, nx])
            cnt += 1
            G[ny][nx] = 9
        y = ny
        x = nx
    return cnt


def solution():
    cctv = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            if G[i][j] == 0:
                cnt += 1
            if 1 <= G[i][j] <= 5:
                cctv.append([i, j, G[i][j]])

    result = cnt
    cctv_len = len(cctv)
    for d in product(range(4), repeat=cctv_len):
        tmp = []
        for i in range(cctv_len):
            y, x = cctv[i][0], cctv[i][1]
            cnt -= change(y, x, dy[d[i]], dx[d[i]], tmp)

            if cctv[i][-1] == 2 or cctv[i][-1] == 5:
                cnt -= change(y, x, -dy[d[i]], -dx[d[i]], tmp)
            if cctv[i][-1] == 3 or cctv[i][-1] == 4 or cctv[i][-1] == 5:
                ddy, ddx = right(dy[d[i]], dx[d[i]])
                cnt -= change(y, x, ddy, ddx, tmp)
            if cctv[i][-1] == 4 or cctv[i][-1] == 5:
                ddy, ddx = right(dy[d[i]], dx[d[i]])
                cnt -= change(y, x, -ddy, -ddx, tmp)

        result = min(result, cnt)
        cnt += len(tmp)
        for y, x in tmp:
            G[y][x] = 0

    print(result)


solution()
