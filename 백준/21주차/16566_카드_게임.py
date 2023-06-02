import sys
import bisect
input = sys.stdin.readline

n, m, k = map(int, input().split())
g = sorted(list(map(int, input().split())))
arr = list(map(int, input().split()))
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

for x in arr:
    i = bisect.bisect_right(g, x)
    result = find(g[i])
    j = bisect.bisect_right(g, result)
    print(result)
    if j < len(g):
        a = find(result)
        b = find(g[j])
        if a != b:
            union(a, b)
