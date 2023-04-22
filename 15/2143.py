import bisect

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

accA = [a[0]]
for i in range(1, len(a)):
    accA.append(accA[-1] + a[i])

accB = [b[0]]
for i in range(1, len(b)):
    accB.append(accB[-1] + b[i])

localA = []
for i in accA:
    localA.append(i)
for i in range(len(accA)):
    for j in range(i+1, len(accA)):
        tmp = accA[j] - accA[i]
        localA.append(tmp)
localA.sort()

localB = []
for i in accB:
    localB.append(i)
for i in range(len(accB)):
    for j in range(i+1, len(accB)):
        tmp = accB[j] - accB[i]
        localB.append(tmp)
localB.sort()

result = 0
for i in localA:
    left = bisect.bisect_left(localB, t - i)
    right = bisect.bisect_right(localB, t - i)
    result += right - left

print(result)
