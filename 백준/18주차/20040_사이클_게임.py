import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

for i in range(1, m+1):
    a, b = map(int, input().split())
    x = find(a)
    y = find(b)
    if x == y:
        print(i)
        exit();
    else:
        union(x, y)

print(0)
