import sys
input = sys.stdin.readline

g = list(input().rstrip())
n = len(g)
result, l, r, acc = 0, 0, 0, 0

for i in range(n):
    if g[i] == '(':
        l += 1
        acc += 1
    else:
        r += 1
        acc -= 1
    if acc == 1:
        l = 0
    elif acc == -1:
        result = r
        break

if acc == 2:
    result = l

print(result)
