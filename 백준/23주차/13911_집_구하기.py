import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
g = [[] for _ in range(v+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    g[u].append([v, w])
    g[v].append([u, w])
m, x = map(int, input().split())
mSet = set(map(int, input().split()))
s, y = map(int, input().split())
sSet = set(map(int, input().split()))

def calc(start):
    dp = [10**9] * (v+1)
    pq = []
    heapq.heappush(pq, [0, start])
    dp[start] = 0
    while pq:
        acc, cur = heapq.heappop(pq)
        for nxt, cost in g[cur]:
            if dp[nxt] > acc + cost:
                dp[nxt] = acc + cost
                heapq.heappush(pq, [acc + cost, nxt])
    mheap = []
    sheap = []
    for a in mSet:
        if dp[a] <= x:
            heapq.heappush(mheap, dp[a])
    for a in sSet:
        if dp[a] <= y:
            heapq.heappush(sheap, dp[a])
    if len(mheap) == 0 or len(sheap) == 0:
        return None
    return heapq.heappop(mheap) + heapq.heappop(sheap)

result = 10**9
for start in range(1, v+1):
    if start not in mSet and start not in sSet:
        tmp = calc(start)
        if tmp != None:
            result = min(result, tmp)
print(result if result != 10**9 else -1)
