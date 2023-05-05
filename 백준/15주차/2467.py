import sys
input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))

s = 0
e = n-1
result = [g[s], g[e]]
while s+1 != e:
    if g[s] + g[e] == 0:
        result = [g[s], g[e]]
        print(*result)
        exit()
    elif g[s] + g[e] > 0:
        e -= 1
    else:
        s += 1
    if abs(g[s] + g[e]) < abs(sum(result)):
            result = [g[s], g[e]]
print(*result)
