import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))

dists = [[10**9] * (n+1) for _ in range(n+1)]

for start in range(1, n+1):
    pq = []
    heappush(pq, [0, start])
    dists[start][start] = 0
    while pq:
        dist, cur = heappop(pq)
        if dists[start][cur] < dist:
            continue
        for nxt, cost in g[cur]:
            if dist + cost < dists[start][nxt]:
                dists[start][nxt] = dist + cost
                heappush(pq, [dist + cost, nxt])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(dists[i][j], end=' ') if dists[i][j] != 10**9 else print(0, end=' ')
    print()
