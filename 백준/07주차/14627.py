from sys import stdin

N, M = map(int, stdin.readline().split())
G = []
for _ in range(N):
    G.append(int(stdin.readline().rstrip('\n')))


def solution():
    start = 1
    end = 1000000000
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for g in G:
            cnt += g // mid

        if cnt >= M:
            start = mid + 1
        else:
            end = mid - 1

    print(sum(G) - end * M)


solution()
