import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, b = map(int, input().split())
    g[u].append([v, 0])
    if b == 1:
        g[v].append([u, 0])
    else:
        g[v].append([u, 1])

dp = [[10**9] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][i] = 0
    pq = []
    heapq.heappush(pq, (0, i))
    while pq:
        acc, cur = heapq.heappop(pq)
        if dp[i][cur] < acc:
            continue
        for nxt, cost in g[cur]:
            if dp[i][nxt] > acc + cost:
                dp[i][nxt] = acc + cost
                heapq.heappush(pq, (dp[i][nxt], nxt))

k = int(input())
for _ in range(k):
    s, e = map(int, input().split())
    print(dp[s][e])
