N, M = map(int, input().split())
G = list(map(int, input().split()))


def solution():
    start = max(G)
    end = sum(G)
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        tmp = 0
        for i in range(N):
            if tmp + G[i] > mid:
                tmp = 0
                cnt += 1
            tmp += G[i]
        if tmp:
            cnt += 1

        if cnt <= M:
            end = mid - 1
        else:
            start = mid + 1

    print(start)


solution()
