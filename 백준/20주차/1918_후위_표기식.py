inorder = input()

stack1 = []
stack2 = []
cur = 0
depth = 0
while cur < len(inorder):
    c = inorder[cur]
    if c == '(':
        depth += 2
        cur += 1
        continue
    if c == ')':
        depth -= 2
        cur += 1
        continue

    ddepth = depth
    if c == '*' or c == '/':
        ddepth += 1
    if c == '+' or c == '-' or c == '*' or c == '/':
        if len(stack2) == 0:
            stack2.append((c, ddepth))
            cur += 1
            continue
        if ddepth <= stack2[-1][1]:
            b = stack1.pop()
            a = stack1.pop()
            c, d = stack2.pop()
            stack1.append(a + b + c)
        else:
            stack2.append((c, ddepth))
            cur += 1
    else:
        stack1.append(c)
        cur += 1

result = ''
for a in stack1:
    result += a
while stack2:
    result += stack2.pop()[0]
print(result)
