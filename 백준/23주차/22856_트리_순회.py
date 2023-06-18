import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n):
    node, l, r = map(int, input().split())
    g[node] = [l, r]

result = -1
def go(start, flag):
    global result
    result += flag
    if flag == 1:
        if g[start][0] != -1:
            go(g[start][0], 2)
        if g[start][1] != -1:
            go(g[start][1], 1)
    if flag == 2:
        if g[start][0] != -1:
            go(g[start][0], 2)
        if g[start][1] != -1:
            go(g[start][1], 2)

go(1, 1)
print(result)
