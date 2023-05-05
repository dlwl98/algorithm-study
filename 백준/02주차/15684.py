from sys import stdin

N, M, H = map(int, stdin.readline().split())
hl = [[False] * N for _ in range(H + 1)]
result = 4
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    hl[a][b] = True


def check():
    for i in range(1, N + 1):
        h = 1
        n = i
        flag = True
        while h <= H:
            if flag:
                if n - 1 and hl[h][n - 1]:
                    n -= 1
                    flag = False
                elif n < N and hl[h][n]:
                    n += 1
                    flag = False
                else:
                    h += 1
                    flag = True
            else:
                h += 1
                flag = True

        if n != i:
            return False
    return True


def dfs(h, n, cnt):
    global result
    if result <= cnt:
        return
    if check():
        result = min(result, cnt)
        return
    if cnt == 3:
        return
    for i in range(h, H + 1):
        k = n if i == h else 1
        for j in range(k, N):
            if not hl[i][j]:
                hl[i][j] = True
                dfs(i, j + 2, cnt + 1)
                hl[i][j] = False


def solution():
    dfs(0, 0, 0)
    if result > 3:
        print(-1)
    else:
        print(result)


solution()
