from sys import stdin
from collections import deque

R, C, M = map(int, stdin.readline().split())
G = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
for _ in range(M):
    r, c, s, d, z = map(int, stdin.readline().split())
    if d <= 2:
        G[r][c] = [s % ((R - 1) * 2), d, z]
    else:
        G[r][c] = [s % ((C - 1) * 2), d, z]
dy = (0, -1, 1, 0, 0)
dx = (0, 0, 0, 1, -1)


def move():
    tmp = deque([])
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if G[i][j]:
                y = i
                x = j
                sp, di, si = G[i][j]
                G[i][j] = []
                for _ in range(sp):
                    if di <= 2:
                        if y == 1 and di == 1:
                            di = 2
                        if y == R and di == 2:
                            di = 1
                        y += dy[di]
                    else:
                        if x == 1 and di == 4:
                            di = 3
                        if x == C and di == 3:
                            di = 4
                        x += dx[di]
                tmp.append([y, x, sp, di, si])
    while tmp:
        y, x, sp, di, si = tmp.popleft()
        if G[y][x] and G[y][x][2] < si:
            G[y][x] = [sp, di, si]
        if not G[y][x]:
            G[y][x] = [sp, di, si]


def solution():
    result = 0
    for j in range(1, C + 1):
        for i in range(1, R + 1):
            if G[i][j]:
                result += G[i][j][2]
                G[i][j] = []
                break
        move()

    print(result)


solution()
