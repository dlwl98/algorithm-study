from itertools import combinations
import bisect
import heapq

n = int(input())
g = sorted(list(map(int, input().split())))

result = []
min_ = 10**10
for i1, i2 in combinations(range(len(g)), 2):
    n1, n2 = g[i1], g[i2]
    tmp = bisect.bisect_left(g, -(n1 + n2))
    if 0 <= tmp < n and g[tmp] == -(n1 + n2):
        if 0 <= tmp < n:
            cur = abs(g[tmp] + n1 + n2)
            if min_ <= cur:
                continue
            if tmp != i1 and tmp != i2:
                result = [n1, n2, g[tmp]]
                min_ = cur
                continue

    arr = []
    if 0 <= tmp < n:
        heapq.heappush(arr, (abs(g[tmp] + n1 + n2), tmp))
    if 0 <= tmp-1 < n:
        heapq.heappush(arr, (abs(g[tmp-1] + n1 + n2), tmp-1))
    if 0 <= tmp+1 < n:
        heapq.heappush(arr, (abs(g[tmp+1] + n1 + n2), tmp+1))

    if arr:
        cur, tmp = heapq.heappop(arr)
        if min_ <= cur:
            continue
        if tmp != i1 and tmp != i2:
            result = [n1, n2, g[tmp]]
            min_ = cur
            continue

result.sort()
print(*result)
