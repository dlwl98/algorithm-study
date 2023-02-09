from sys import stdin
from functools import cmp_to_key
import heapq

N, K = map(int, stdin.readline().split())
G = [list(map(int, stdin.readline().split())) for _ in range(N)]
bags = [int(stdin.readline().rstrip('\n')) for _ in range(K)]


def sort_by_first(x, y):
    return x[0] - y[0]큐


def solution():
    G.sort(key=cmp_to_key(sort_by_first))
    bags.sort()

    result = 0
    i = 0
    pq = []
    for bag in bags:
        while i < N and bag >= G[i][0]:
            heapq.heappush(pq, -G[i][1])
            i += 1
        if pq:
            result += heapq.heappop(pq)
    print(-result)


solution()
