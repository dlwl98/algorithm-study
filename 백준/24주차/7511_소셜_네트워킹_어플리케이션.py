import sys
input = sys.stdin.readline

tc = int(input())
for i in range(1, tc+1):
    print(f"Scenario {i}:")
    n = int(input())
    parent = [i for i in range(n+1)]

    def find(x):
        if parent[x] == x:
            return parent[x]
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        a = find(x)
        b = find(y)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        print(1 if find(a) == find(b) else 0)
    print()
