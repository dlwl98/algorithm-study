from collections import deque
from sys import stdin

N = int(stdin.readline().rstrip('\n'))
G = [int(stdin.readline().rstrip('\n')) for _ in range(N)]


def solution():
    result = 0
    s = deque()
    for i in range(N):
        if len(s) == 0:
            s.append([G[i], 1])
            continue

        while len(s) != 0 and s[-1][0] < G[i]:
            g, cnt = s.pop()
            result += cnt

        if len(s) != 0:
            if s[-1][0] == G[i]:
                result += s[-1][1]
                if len(s) >= 2:
                    result += 1
                s[-1][1] += 1
            if s[-1][0] > G[i]:
                s.append([G[i], 1])
                result += 1
        else:
            s.append([G[i], 1])

    print(result)


solution()
