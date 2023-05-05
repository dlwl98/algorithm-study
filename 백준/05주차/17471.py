from collections import deque
from itertools import combinations


def minus_one(num):
    return num - 1


N = int(input())
pop = list(map(int, input().split()))
sum_pop = sum(pop)
G = [[] for _ in range(10)]

for k in range(N):
    tmp = deque(map(int, input().split()))
    tmp.popleft()
    G[k] = list(map(minus_one, tmp))


def check(arr):
    cnt = 0
    g = [False] * N
    for i in arr:
        g[i] = True

    visited = [False] * N

    start = 0
    for i in range(N):
        if g[i]:
            start = i
            break

    queue = deque([start])
    visited[start] = True
    cnt += 1
    while queue:
        cur = queue.popleft()
        for n in G[cur]:
            if not visited[n] and g[n]:
                visited[n] = True
                queue.append(n)
                cnt += 1

    for i in range(N):
        if not g[i]:
            start = i
            break

    queue = deque([start])
    visited[start] = True
    cnt += 1
    while queue:
        cur = queue.popleft()
        for n in G[cur]:
            if not visited[n] and not g[n]:
                visited[n] = True
                queue.append(n)
                cnt += 1

    return True if cnt == N else False


def solution():
    result = sum_pop

    idx = [i for i in range(N)]
    for i in range(1, N // 2 + 1):
        combs = combinations(idx, i)
        for comb in combs:
            if check(comb):
                s = 0
                for a in comb:
                    s += pop[a]

                result = min(result, abs(s - (sum_pop - s)))

    print(result if result != sum_pop else -1)


solution()
