from collections import deque

n = int(input())
g = {}
for i in range(65, 91):
    g[chr(i)] = set()
for i in range(97, 123):
    g[chr(i)] = set()

for _ in range(n):
    pre, _, post = input().split()
    g[pre].add(post)

result = set()
for a in g.keys():
    v = {}
    for b in g.keys():
        v[b] = False
    v[a] = True
    q = deque([a])
    while q:
        cur = q.popleft()
        for nxt in g[cur]:
            if not v[nxt]:
                result.add((a, nxt))
                v[nxt] = True
                q.append(nxt)

result = sorted(list(result))
print(len(result))
for s, e in result:
    print(s, end=' ')
    print('=>', end=' ')
    print(e)
