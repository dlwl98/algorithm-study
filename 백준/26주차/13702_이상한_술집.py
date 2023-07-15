import sys
input = sys.stdin.readline

n, k = map(int, input().split())
g = [int(input()) for _ in range(n)]

s = 0
e = 2 ** 31
while s <= e:
    mid = (s + e) // 2
    tmp = 0
    for a in g:
        tmp += a // mid
    if tmp >= k:
        s = mid + 1
    else:
        e = mid - 1

print(e)
