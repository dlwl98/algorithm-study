from functools import cmp_to_key
from collections import deque
import heapq

n = int(input())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
g = deque()

def custom_sort(x, y):
    if x[0] == y[0]:
        return y[1] - x[1]
    return x[0] - y[0]

def to_days(a, b):
    result = 0
    for i in range(1, 13):
        if i >= a:
            break
        result += month[i]
    return result + b

start = to_days(3, 1)
end = to_days(11, 30)

for _ in range(n):
    a, b, c, d = map(int, input().split())
    x = to_days(a, b)
    y = to_days(c, d)
    if y > start and x <= end:
        g.append([max(start, x), min(y, end+1)])

flowers = sorted(g, key=cmp_to_key(custom_sort))

result = 1
i = 0

while i < len(flowers):
    pq = []
    j = i + 1
    while j < len(flowers):
        if flowers[j][0] <= flowers[i][1]:
            if flowers[i][1] < flowers[j][1]:
                heapq.heappush(pq, [-flowers[j][1], j])
        else:
            break
        j += 1
    if pq:
        result += 1
        cost, i = heapq.heappop(pq)
    else:
        break

if flowers[i][1] != end + 1 or flowers[0][0] != 60:
    print(0)
else:
    print(result)
