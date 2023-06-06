import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

g = [[] for _ in range(n+1)]
for a, b, c in arr:
    g[a].append([b, c])
    g[b].append([a, c])

dist = [10**9] * (n+1)
dist[s] = 0
pq = []
heapq.heappush(pq, [0, s])

while pq:
    acc, cur = heapq.heappop(pq)
    for nxt, cost in g[cur]:
        if acc + cost < dist[nxt]:
            dist[nxt] = acc + cost
            heapq.heappush(pq, [dist[nxt], nxt])

print(dist[t])
