n = int(input())
a, b, c, d = [], [], [], []
for _ in range(n):
    n1, n2, n3, n4 = map(int, input().split())
    a.append(n1)
    b.append(n2)
    c.append(n3)
    d.append(n4)

dic = {}
for i in range(n):
    for j in range(n):
        if a[i] + b[j] in dic:
            dic[a[i] + b[j]] += 1
        else:
            dic[a[i] + b[j]] = 1

result = 0

for i in range(n):
    for j in range(n):
        if -(c[i] + d[j]) in dic:
            result += dic[-(c[i] + d[j])]

print(result)
