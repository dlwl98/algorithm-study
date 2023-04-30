import sys
from functools import cmp_to_key
input = sys.stdin.readline

[n, m] = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n + 1)]

def sortBycost(a, b):
    return a[2] - b[2]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges.sort(key=cmp_to_key(sortBycost))
result = []

for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b)
        result.append(cost)

print(sum(result) - result[-1])
