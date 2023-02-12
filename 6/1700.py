from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
G = list(map(int, stdin.readline().split()))
idx_stack = [deque() for _ in range(K+1)]
for a in range(K):
    idx_stack[G[a]].append(a)


def solution():
    cnt = 0
    rest = N
    using = [False] * (K+1)
    for i in range(K):
        if using[G[i]]:
            idx_stack[G[i]].popleft()
            continue
        if rest != 0:
            idx_stack[G[i]].popleft()
            rest -= 1
            using[G[i]] = True
        else:
            tmp = 0
            for j in range(1, K+1):
                if G[i] == j or not using[j]:
                    continue
                if len(idx_stack[j]) == 0:
                    tmp = j
                    break
                else:
                    if tmp == 0:
                        tmp = j
                    else:
                        if idx_stack[tmp][0] < idx_stack[j][0]:
                            tmp = j
            using[tmp] = False
            cnt += 1
            idx_stack[G[i]].popleft()
            using[G[i]] = True

    print(cnt)


solution()
