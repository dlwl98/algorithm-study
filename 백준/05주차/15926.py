from sys import stdin

N = int(input())
G = stdin.readline().rstrip('\n')


def solution():
    s = []
    idx = []
    for i in range(1, N+1):
        if len(s) > 0 and s[-1] == '(' and G[i-1] == ')':
            s.pop()
            idx.pop()
        else:
            s.append(G[i-1])
            idx.append(i)
    idx.append(N+1)

    tmp = 0
    result = 0
    for i in idx:
        result = max(result, i - tmp - 1)
        tmp = i

    print(result)


solution()
