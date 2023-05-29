n = int(input())

result = 1
for i in range(2, n):
    if i % 2 == 1:
        if n % i == 0 and n // i > i // 2:
            result += 1
    else:
        if n % i == i // 2 and n // i >= i // 2:
            result += 1

print(result)
