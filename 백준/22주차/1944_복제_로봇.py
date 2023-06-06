import sys
from collections import deque
from functools import cmp_to_key
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(input().rstrip()) for _ in range(n)]
start = [0, 0]
keys = []
parent = [i for i in range(m+1)]
for i in range(n):
    for j in range(n):
        if g[i][j] == 'S':
            start = [i, j]
            keys.append([i, j])
        if g[i][j] == 'K':
            keys.append([i, j])

def inRange(y, x):
    return 0 <= y < n and 0 <= x < n

def mycmp(a, b):
    return a[0] - b[0]

def bfs(a, b):
    q = deque()
    v = [[False] * n for _ in range(n)]
    v[a[0]][a[1]] = True
    q.append([0, a])
    while q:
        [dist, [y, x]] = q.popleft()
        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny = y + dy
            nx = x + dx
            if [ny, nx] == b:
                return dist + 1
            if inRange(ny, nx) and g[ny][nx] != '1' and not v[ny][nx]:
                v[ny][nx] = True
                q.append([dist + 1, [ny, nx]])
    print(-1)
    exit()

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

lines = []
for i in range(m+1):
    for j in range(i, m+1):
        lines.append([bfs(keys[i], keys[j]), i, j])
lines.sort(key=cmp_to_key(mycmp))

result = 0
cnt = 0
for cost, i, j in lines:
    a = find(i)
    b = find(j)
    if a != b:
        cnt += 1
        result += cost
        union(a, b)
        if cnt == m:
            break

if cnt == m: 
    print(result)
else: 
    print(-1)
