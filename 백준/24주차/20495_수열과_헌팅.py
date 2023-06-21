import sys
from bisect import bisect_right, bisect_left
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

minarr = []
maxarr = []
for a, b in g:
    minarr.append(a - b)
    maxarr.append(a + b)

minarr.sort()
maxarr.sort()

for i in range(n):
    minidx = bisect_left(maxarr, g[i][0] - g[i][1])
    maxidx = bisect_right(minarr, g[i][0] + g[i][1])
    print(minidx + 1, maxidx)
    
