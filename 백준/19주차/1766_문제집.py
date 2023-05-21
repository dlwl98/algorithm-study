n, m = map(int, input().split())
ind = [0] * (n+1)
g = [[] for _ in range(n+1)]
v = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    ind[b] += 1

result = []

def find():
    for i in range(1, n+1):
        if v[i]: continue
        if ind[i] == 0:
            result.append(i)
            v[i] = True
            for nxt in g[i]:
                ind[nxt] -= 1
            return

for i in range(1, n+1):
    find()

print(*result)
