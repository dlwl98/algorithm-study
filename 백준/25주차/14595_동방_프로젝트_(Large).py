import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    x, y = map(int, input().split())
    while x < y:
        if x != find(x):
            x = find(x)
            continue
        union(x, y)
        x += 1

result = 0
for i in range(1, n+1):
    if i == find(i):
        result += 1

print(result)
