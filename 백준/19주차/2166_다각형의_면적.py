def tri(a,d,b,e,c,f):
    first = (a * e) + (b * f) + (c * d)
    second = (d * b) + (e * c) + (f * a)
    re = (first - second) * 0.5
    return re

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
start = g[0]

result = 0
for i in range(2, n):
    result += tri(start[0], start[1], g[i][0], g[i][1], g[i-1][0], g[i-1][1])

print(abs(result))
