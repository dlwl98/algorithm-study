import bisect

n = int(input())
a = [False, False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

tmp = 0
acc = [0]
for i in primes:
    tmp += i
    acc.append(tmp)

result = 0
for i in acc:
    a = bisect.bisect_left(acc, i + n)
    if 0 <= a < len(acc) and acc[a] == i + n:
        result += 1

print(result)
