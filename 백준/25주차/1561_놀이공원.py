import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = list(map(int, input().split()))

s = 0
e = 6 * 10**10
while s <= e:
    mid = (s + e) // 2
    acc = 0
    for a in g:
        acc += mid // a + 1
    if acc >= n:
        e = mid - 1
    else:
        s = mid + 1

tmp = 0
for a in g:
    tmp += e // a + 1

result = tmp
for i in range(m):
    if (e + 1) % g[i] == 0:
        result += 1
    if result == n:
        print(i + 1)
        exit()
