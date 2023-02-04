from sys import stdin

N = int(input())
G = [list(stdin.readline().rstrip('\n')) for _ in range(N)]


def solution():
    result = N * N
    for flag in range(1 << N):
        cnt = 0
        for x in range(N):
            tmp = 0
            for y in range(N):
                if flag & (1 << y):
                    if G[y][x] == 'H':
                        tmp += 1
                else:
                    if G[y][x] == 'T':
                        tmp += 1
            cnt += min(tmp, N - tmp)
        result = min(result, cnt)
    print(result)


solution()
