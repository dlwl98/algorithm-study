n = int(input())
stock = list(map(int, input().split()))

a = [n, 0]
for i in range(14):
    if a[0] // stock[i]:
        a[1] += a[0] // stock[i]
        a[0] -= a[0] // stock[i] * stock[i]

b = [n, 0]
upDown = [[] for _ in range(14)]
upDown[0] = 0
for i in range(1, 14):
    if stock[i-1] < stock[i]:
        if upDown[i-1] > 0:
            upDown[i] = upDown[i-1] + 1
        else:
            upDown[i] = 1
    elif stock[i-1] > stock[i]:
        if upDown[i-1] < 0:
            upDown[i] = upDown[i-1] - 1
        else:
            upDown[i] = -1
    else:
        upDown[i] = 0

for i in range(14):
    if upDown[i] >= 3:
        b[0] += b[1] * stock[i]
        b[1] = 0
    elif upDown[i] <= -3:
        b[1] += b[0] // stock[i]
        b[0] -= b[0] // stock[i] * stock[i]

resulta = a[0] + stock[-1] * a[1]
resultb = b[0] + stock[-1] * b[1]

if resulta > resultb:
    print("BNP")
elif resulta < resultb:
    print("TIMING")
else:
    print("SAMESAME")
