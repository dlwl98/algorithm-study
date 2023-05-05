from sys import stdin

n = int(input())
g = sorted([tuple(map(int, stdin.readline().split())) for _ in range(n)])

l = g[0][0]
r = g[0][1]
result = 0
for s, e in g:
    if s < r:
        r = max(r, e)
    else:
        result += r - l
        l = s
        r = e

result += r - l
print(result)
