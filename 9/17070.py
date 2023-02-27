N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
cnt = 0


def dfs(y, x, flag):
    global cnt
    if y == N - 1 and x == N - 1:
        cnt += 1
        return
    if y + 1 < N and x + 1 < N:
        if G[y + 1][x + 1] == 0 and G[y][x + 1] == 0 and G[y + 1][x] == 0:
            dfs(y + 1, x + 1, 1)

    if flag == 0 or flag == 1:
        if x + 1 < N:
            if G[y][x + 1] == 0:
                dfs(y, x + 1, 0)

    if flag == 1 or flag == 2:
        if y + 1 < N:
            if G[y + 1][x] == 0:
                dfs(y + 1, x, 2)


def solution():
    dfs(0, 1, 0)
    print(cnt)


solution()
