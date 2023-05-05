from sys import stdin

dy = (0, -1, 1, 0, 0)
dx = (0, 0, 0, -1, 1)
N, M, K = map(int, stdin.readline().split())
G = [list(map(int, stdin.readline().split())) for _ in range(N)]
D = list(map(int, stdin.readline().split()))

# shark[상어 번호][상어 y, 상어 x, 방향, 상태]
shark = [[0] * 4 for _ in range(M + 1)]
for i in range(N):
    for j in range(N):
        if G[i][j] > 0:
            shark[G[i][j]] = [i, j, D[G[i][j] - 1], True]

# small[상어 y][상어 x][상어 번호, 남은 시간]
small = [[[0] * 2 for _ in range(N)] for _ in range(N)]

# shark[상어 번호][방향][우선 순위]
info = [[[0] * 4 for _ in range(5)] for _ in range(M + 1)]

for i in range(1, M+1):
    for j in range(1, 5):
        tmp = list(map(int, stdin.readline().split()))
        info[i][j] = tmp


def move(s, tick):
    y, x, d, status = shark[s]
    if not status:
        return
    for h in info[s][d]:
        ny = y + dy[h]
        nx = x + dx[h]
        if 0 <= ny < N and 0 <= nx < N and small[ny][nx][1] - tick <= 0:
            shark[s] = [ny, nx, h, True]
            return

    for h in info[s][d]:
        ny = y + dy[h]
        nx = x + dx[h]
        if 0 <= ny < N and 0 <= nx < N and small[ny][nx][0] == s:
            shark[s] = [ny, nx, h, True]
            return
    return


def solution():
    for s in range(1, M + 1):
        small[shark[s][0]][shark[s][1]] = [s, K]

    cnt = M
    tick = 0
    while cnt > 1:
        if tick >= 1000:
            print(-1)
            return

        for s in range(1, M+1):
            if not shark[s][-1]:
                continue
            move(s, tick)

        tick += 1

        for s in range(1, M + 1):
            if not shark[s][-1]:
                continue
            a, b = small[shark[s][0]][shark[s][1]]
            if b == K + tick:
                if s > a:
                    small[shark[s][0]][shark[s][1]][0] = a
                    shark[s][-1] = False
                else:
                    shark[a][-1] = False
                cnt -= 1
            else:
                small[shark[s][0]][shark[s][1]] = [s, K + tick]

    print(tick)


solution()
