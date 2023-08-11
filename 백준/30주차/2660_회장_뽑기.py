import heapq
import sys
input = sys.stdin.readline

n = int(input())
g =  [[] for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    g[a].append(b)
    g[b].append(a)

dp = [[10**9] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][i] = 0
    pq = []
    heapq.heappush(pq, [0, i])
    while pq:
        acc, cur = heapq.heappop(pq)
        if dp[i][cur] < acc:
            continue
        for nxt in g[cur]:
            if dp[i][nxt] > acc + 1:
                dp[i][nxt] = acc + 1
                heapq.heappush(pq, [acc + 1, nxt])

for i in range(1, n+1):
    dp[i][0] = 0

scores = [max(tmp) for tmp in dp]
min_score = min(scores)
print(min_score, scores.count(min_score))
for i in range(1, n+1):
    if scores[i] == min_score:
        print(i, end=' ')
