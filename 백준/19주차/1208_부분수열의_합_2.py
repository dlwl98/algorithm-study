from itertools import combinations
import bisect

n, s = map(int, input().split())
g = list(map(int, input().split()))

a = n // 2
b = n - a
ga = g[0:a]
gb = g[a:]
acca = []
accb = []
result = 0

for i in range(1, a+1):
    for com in combinations(ga, i):
        tmp = sum(com)
        acca.append(tmp)
        if tmp == s:
            result += 1


for i in range(1, b+1):
    for com in combinations(gb, i):
        tmp = sum(com)
        accb.append(tmp)
        if tmp == s:
            result += 1

accb.sort()

for i in acca:
    find = s-i
    resl = bisect.bisect_left(accb, find)
    resr = bisect.bisect_right(accb, find)
    result += resr - resl

print(result)
