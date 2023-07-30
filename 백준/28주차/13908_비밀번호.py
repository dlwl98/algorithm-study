from itertools import product

n, m = map(int, input().split())
if m == 0:
    print(10 ** n)
    exit()

s = set(map(int, input().split()))

result = 0
for t in product(range(10), repeat=n):
    tmp = set()
    for a in t:
        if a in s:
            tmp.add(a)
    if len(tmp) == m:
        result += 1
        
print(result)
