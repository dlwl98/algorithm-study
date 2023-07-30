from collections import deque
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    g[s].append([e, c])
    g[e].append([s, c])
s, e = map(int, input().split())

def dijkstra():
    dist = [10**9] * (n+1)
    prev = [-1] * (n+1)
    pq = []
    heapq.heappush(pq, (0, s))
    while pq:
        acc, cur = heapq.heappop(pq)
        if dist[cur] < acc:
            continue
        for nxt, cost in g[cur]:
            if dist[nxt] >= acc + cost:
                if dist[nxt] == acc + cost:
                    if prev[nxt] != -1 and prev[nxt] > cur:
                        dist[nxt] = acc + cost
                        heapq.heappush(pq, (acc + cost, nxt))
                        prev[nxt] = cur
                else:
                    dist[nxt] = acc + cost
                    heapq.heappush(pq, (acc + cost, nxt))
                    prev[nxt] = cur
    path = []
    cur = prev[e]
    while cur != s:
        path.append(cur)
        cur = prev[cur]

    return [dist[e], set(path)]

result, visitedSet = dijkstra()

dist = [10**9] * (n+1)
pq = []
heapq.heappush(pq, (0, e))
while pq:
    acc, cur = heapq.heappop(pq)
    if dist[cur] < acc:
        continue
    for nxt, cost in g[cur]:
        if nxt in visitedSet:
            continue
        if dist[nxt] > acc + cost:
            dist[nxt] = acc + cost
            heapq.heappush(pq, (acc + cost, nxt))

print(result + dist[s])
