from sys import stdin
import heapq

n, m, x = map(int, stdin.readline().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, cost = map(int, stdin.readline().split())
    g[s].append([e, cost])

min_dist = [[10 ** 9] * (n + 1) for _ in range(n + 1)]

for start in range(1, n + 1):
    q = []
    min_dist[start][start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, cur = heapq.heappop(q)
        if min_dist[start][cur] < dist:
            continue
        for next_, cost in g[cur]:
            if dist + cost < min_dist[start][next_]:
                min_dist[start][next_] = dist + cost
                heapq.heappush(q, (dist + cost, next_))

result = 0
for i in range(1, n + 1):
    result = max(result, min_dist[i][x] + min_dist[x][i])
print(result)
