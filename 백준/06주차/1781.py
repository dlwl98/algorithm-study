from sys import stdin
import heapq

N = int(stdin.readline())
G = [list(map(int, stdin.readline().split())) for _ in range(N)]


def solution():
    G.sort()
    pq = []
    for deadline, cup in G:
        heapq.heappush(pq, cup)
        if deadline < len(pq):
            heapq.heappop(pq)

    print(sum(pq))


solution()
