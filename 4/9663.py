N = int(input())
G = [[0] * N for _ in range(N)]
can_put = [[True] * N for _ in range(N)]
result = 0
dy = (-1, 1, 0, 0, -1, 1, -1, 1)
dx = (0, 0, -1, 1, 1, 1, -1, -1)


def change(i, j):
    changes = [(i, j)]
    can_put[i][j] = False
    for k in range(N):
        for n in range(8):
            ni = i + dy[n] * k
            nj = j + dx[n] * k
            if 0 <= ni < N and 0 <= nj < N and can_put[ni][nj]:
                changes.append((ni, nj))
                can_put[ni][nj] = False
    return changes


def dfs(y, x, depth):
    global result
    if depth == N:
        result += 1
        return
    for i in range(y, N):
        if i != y:
            x = 0
        for j in range(x, N):
            if can_put[i][j]:
                changes = change(i, j)
                dfs(i, j, depth + 1)
                for a, b in changes:
                    can_put[a][b] = True


def solution():
    dfs(0, 0, 0)
    print(result)


solution()
