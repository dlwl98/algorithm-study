from sys import stdin
import math

n, m, k = map(int, stdin.readline().split())
g = [0] + [int(stdin.readline()) for _ in range(n)]
h = math.ceil(math.log2(n))
tree = [-1 for _ in range(1 << (h + 1))]

def go(i, l, r):
    if l == r:
        tree[i] = g[l]
        return g[l]
    tree[i] = go(i*2, l, (l+r)//2) + go(i*2+1, (l+r)//2+1, r)

    return tree[i]

go(1, 1, n)

def update(i, l, r, target, diff):
    if l <= target <= r:
        tree[i] += diff
        if l == r:
            return
        update(i*2, l, (l+r)//2, target, diff)
        update(i*2+1, (l+r)//2+1, r, target, diff)

def cal(i, l, r, tl, tr):
    if l >= tl and r <= tr:
        return tree[i]
    if tl > r or tr < l:
        return 0

    return cal(i*2, l, (l+r)//2, tl, tr) + cal(i*2+1, (l+r)//2+1, r, tl, tr)

for _ in range(m + k):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        diff = c - g[b]
        g[b] = c
        update(1, 1, n, b, diff)
    if a == 2:
        print(cal(1, 1, n, b, c))
