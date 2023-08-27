from functools import cmp_to_key
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def my_cmp(a, b):
    if a[0] == b[0]:
        return a[1] - b[1]
    return a[0] - b[0]

n = int(input())
g = sorted([list(map(int, input().split())) for _ in range(n)], key=cmp_to_key(my_cmp))
m = 0
for p, d in g:
    m = max(m, d)
result = [0] * (m+1)

def push(p, d):
    if d == 0:
        return
    if result[d] == 0:
        result[d] = p
        return
    push(p, d-1)

while g:
    p, d = g.pop()
    push(p, d)

print(sum(result))
