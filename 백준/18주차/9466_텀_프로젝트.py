import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    g = [0] + list(map(int, input().split()))
    degree = [0] * (n+1)
    for i in range(1, n+1):
        degree[g[i]] += 1

    q = deque()
    cnt = 0
    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)
            cnt += 1

    while q:
        cur = q.popleft()
        degree[g[cur]] -= 1
        if degree[g[cur]] == 0:
            q.append(g[cur])
            cnt += 1
    
    print(cnt)

