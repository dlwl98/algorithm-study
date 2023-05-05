n = int(input())
h = [int(input()) for _ in range(n)]

stack = []
result = [0] * n
for i in range(n):
    while stack and stack[-1][0] <= h[i]:
        result[stack[-1][1]] = len(stack) - 1
        stack.pop()

    stack.append((h[i], i))

for i in range(len(stack)):
    _, j = stack[i]
    result[j] = len(stack) - i - 1

print(sum(result))
