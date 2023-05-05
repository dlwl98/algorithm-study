from sys import stdin

N, L = map(int, stdin.readline().split())
G = [list(map(int, stdin.readline().split())) for _ in range(N)]


def row_check(i):
    put = [False] * N
    j = 0
    before = -1
    while j < N:
        if j != 0:
            if before + 1 == G[i][j]:
                for k in range(L, 0, -1):
                    if j-k < 0:
                        return False
                    if G[i][j-k] != before:
                        return False
                    if put[j-k]:
                        return False
                    put[j-k] = True
            elif before == G[i][j] + 1:
                for k in range(L):
                    if j+k >= N:
                        return False
                    if G[i][j+k] != G[i][j]:
                        return False
                    if put[j+k]:
                        return False
                    put[j+k] = True
            elif abs(before - G[i][j]) > 1:
                return False

        before = G[i][j]
        j += 1

    return True


def col_check(i):
    put = [False] * N
    j = 0
    before = -1
    while j < N:
        if j != 0:
            if before + 1 == G[j][i]:
                for k in range(L, 0, -1):
                    if j-k < 0:
                        return False
                    if G[j-k][i] != before:
                        return False
                    if put[j-k]:
                        return False
                    put[j-k] = True
            elif before == G[j][i] + 1:
                for k in range(L):
                    if j+k >= N:
                        return False
                    if G[j+k][i] != G[j][i]:
                        return False
                    if put[j+k]:
                        return False
                    put[j+k] = True
            elif abs(before - G[j][i]) > 1:
                return False

        before = G[j][i]
        j += 1

    return True


def solution():
    cnt = 0
    for i in range(N):
        if row_check(i):
            cnt += 1
    for i in range(N):
        if col_check(i):
            cnt += 1

    print(cnt)


solution()
