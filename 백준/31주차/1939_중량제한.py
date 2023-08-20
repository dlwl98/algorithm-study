from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])
p1, p2 = map(int, input().split())

def canGo(weight):
    v = [False] * (n+1)
    v[p1] = True
    q = deque([p1])
    while q:
        cur = q.popleft()
        if cur == p2:
            return True
        for nxt, maxWeight in g[cur]:
            if not v[nxt] and weight <= maxWeight :
                v[nxt] = True
                q.append(nxt)
    return False

s = 1
e = 10**9
while s <= e:
    mid = (s + e) // 2
    if canGo(mid):
        s = mid + 1
    else:
        e = mid - 1

print(e)
