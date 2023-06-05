import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
g = list(map(int, input().split()))
v = {}
q = deque()
for a in g:
    q.append([a, 1])
    v[a] = 0

while q:
    cur, d = q.popleft()
    if cur-d not in v:
        v[cur-d] = d
        q.append([cur, d+1])
    if len(v) == n+k:
        break
    if cur+d not in v:
        v[cur+d] = d
        q.append([cur, d+1])
    if len(v) == n+k:
        break

result = 0
for a in v:
    result += v[a]
print(result)
