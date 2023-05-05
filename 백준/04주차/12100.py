N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
result = 0


def dfs(depth, g):
    global result
    if depth == 5:
        result = max(result, max(map(max, g)))
        return

    # 왼쪽
    move = [[0] * N for _ in range(N)]
    for i in range(N):
        k = 0
        for j in range(N):
            if g[i][j] != 0:
                move[i][k] = g[i][j]
                k += 1

    tmp = [[0] * N for _ in range(N)]
    flag = False
    for _ in range(2):
        for i in range(N):
            k = 0
            for j in range(N):
                if flag:
                    flag = False
                    continue
                if move[i][j] != 0:
                    if j+1 < N and move[i][j] == move[i][j+1]:
                        tmp[i][k] = move[i][j] * 2
                        flag = True
                    else:
                        tmp[i][k] = move[i][j]
                    k += 1
    dfs(depth + 1, tmp)

    # 오른쪽
    move = [[0] * N for _ in range(N)]
    for i in range(N):
        k = N - 1
        for j in range(N - 1, -1, -1):
            if g[i][j] != 0:
                move[i][k] = g[i][j]
                k -= 1

    tmp = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        k = N - 1
        for j in range(N - 1, -1, -1):
            if flag:
                flag = False
                continue
            if move[i][j] != 0:
                if j - 1 >= 0 and move[i][j] == move[i][j - 1]:
                    tmp[i][k] = move[i][j] * 2
                    flag = True
                else:
                    tmp[i][k] = move[i][j]
                k -= 1
    dfs(depth + 1, tmp)

    # 위쪽
    move = [[0] * N for _ in range(N)]
    for i in range(N):
        k = 0
        for j in range(N):
            if g[j][i] != 0:
                move[k][i] = g[j][i]
                k += 1

    tmp = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        k = 0
        for j in range(N):
            if flag:
                flag = False
                continue
            if move[j][i] != 0:
                if j + 1 < N and move[j][i] == move[j + 1][i]:
                    tmp[k][i] = move[j][i] * 2
                    flag = True
                else:
                    tmp[k][i] = move[j][i]
                k += 1
    dfs(depth + 1, tmp)

    # 아래쪽
    move = [[0] * N for _ in range(N)]
    for i in range(N):
        k = N - 1
        for j in range(N-1, -1, -1):
            if g[j][i] != 0:
                move[k][i] = g[j][i]
                k -= 1

    tmp = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        k = N - 1
        for j in range(N - 1, -1, -1):
            if flag:
                flag = False
                continue
            if move[j][i] != 0:
                if j - 1 >= 0 and move[j][i] == move[j - 1][i]:
                    tmp[k][i] = move[j][i] * 2
                    flag = True
                else:
                    tmp[k][i] = move[j][i]
                k -= 1
    dfs(depth + 1, tmp)


def solution():
    dfs(0, G)
    print(result)


solution()
