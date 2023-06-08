import sys
import heapq
input = sys.stdin.readline

n, m, x, y = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])

def dijkstra(start):
    dp = [10**9] * n
    pq = []
    dp[start] = 0
    heapq.heappush(pq, [0, start])
    while pq:
        dist, cur = heapq.heappop(pq)
        for nxt, cost in g[cur]:
            if dp[nxt] > dist + cost:
                dp[nxt] = dist + cost
                heapq.heappush(pq, [dist + cost, nxt])
    
    return dp

distance = dijkstra(y)

houses = []
for i in range(n):
    if i == y: continue
    houses.append([distance[i], i])
houses.sort()

if houses[-1][0] * 2 > x: 
    print(-1)
else:
    day = 1
    cur = 0
    for dist, house in houses:
        if cur + 2 * dist <= x:
            cur += 2 * dist
        else:
            day += 1
            cur = 2 * dist
    print(day)
