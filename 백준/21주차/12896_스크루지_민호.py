import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
status = [list(map(int, input().split())) for _ in range(n-1)]
g = [[] for _ in range(n+1)]
for a, b in status:
    g[a].append(b)
    g[b].append(a)

tmp = [0, 0]
v = [False] * (n+1)

def go(i, acc):
    if acc > tmp[1]:
        tmp[0] = i
        tmp[1] = acc
    for nxt in g[i]:
        if not v[nxt]:
            v[nxt] = True
            go(nxt, acc+1)

v[1] = True
go(1, 0)
v = [False] * (n+1)
v[tmp[0]] = True
go(tmp[0], 0)
print(tmp[1] // 2 + 1 if tmp[1] % 2 else tmp[1] // 2)
