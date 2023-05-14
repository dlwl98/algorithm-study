import sys
import bisect
input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))

result = [g[0]]

for x in g:
    if x > result[-1]:
        result.append(x)
    else:
        i = bisect.bisect_left(result, x)
        result[i] = x

print(len(result))
