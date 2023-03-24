n = int(input())
a = [False, False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
primes += [0]

i = 0
j = 0
tmp = primes[i]
result = 0

while j < len(primes) - 1:
    if tmp == n:
        result += 1
        tmp -= primes[i]
        i += 1
        j += 1
        tmp += primes[j]
    elif tmp < n:
        j += 1
        tmp += primes[j]
    else:
        tmp -= primes[i]
        i += 1

print(result)
