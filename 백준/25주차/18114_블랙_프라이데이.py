import bisect
from itertools import combinations
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
g = sorted(list(map(int, input().split())))

if c in g:
    print(1)
    exit()

s = 0
e = n-1
while s < e:
    if g[s] + g[e] == c:
        print(1)
        exit()
    if g[s] + g[e] > c:
        e -= 1
        continue
    tmp = c - g[s] - g[e]
    if g[s] != tmp and g[e] != tmp:
        idx = bisect.bisect_left(g, tmp)
        if idx < n and g[idx] == tmp:
            print(1)
            exit()
    s += 1

print(0)
