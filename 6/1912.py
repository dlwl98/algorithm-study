N = int(input())
G = list(map(int, input().split()))


def solution():
    tmp = 0
    result = []
    for g in G:
        tmp += g
        if tmp < g:
            tmp = g
        result.append(tmp)

    print(max(result))


solution()
