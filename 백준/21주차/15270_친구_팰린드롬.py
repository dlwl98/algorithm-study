import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(m)]
v = [0] * (n+1)

result = 0
def go(i, cnt):
    global result
    result = max(result, cnt)
    if result > cnt + n - sum(v):
        return
    if i >= m:
        return
    if not v[g[i][0]] and not v[g[i][1]]:
        v[g[i][0]] = 1
        v[g[i][1]] = 1
        go(i+1, cnt+2)
        v[g[i][0]] = 0
        v[g[i][1]] = 0
        go(i+1, cnt)
    else:
        go(i+1, cnt)

go(0, 0)
print(result if result >= n else result + 1)
