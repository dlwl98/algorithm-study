n, d, k, c = map(int, input().split())
g = [int(input()) for _ in range(n)]

result = 0
for i in range(n):
    s = set()
    for j in range(i, i+k):
        s.add(g[j % n])
    s.add(c)
    result = max(result, len(s))

print(result)
