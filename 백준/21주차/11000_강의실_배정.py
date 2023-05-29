import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    s, e = map(int, input().split())
    heappush(pq, (s, 's'))
    heappush(pq, (e, 'e'))

result = 0
cur = 0
while pq:
    t, kind = heappop(pq)
    if kind == 's':
        cur += 1
    else:
        cur -= 1
    result = max(result, cur)

print(result)
