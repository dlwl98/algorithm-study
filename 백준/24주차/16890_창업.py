import sys
from collections import deque
input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = list(input().rstrip())
n = len(s1)
s1.sort()
s2.sort(reverse=True)
s1 = deque(s1[:(n+1)//2])
s2 = deque(s2[:n // 2])

result1 = deque()
result2 = deque()
for i in range(n):
    if i % 2 == 0:
        if not s2 or s1[0] < s2[0]:
            result1.append(s1.popleft())
        else:
            result2.appendleft(s1.pop())
    else:
        if not s1 or s1[0] < s2[0]:
            result1.append(s2.popleft())
        else:
            result2.appendleft(s2.pop())

print(''.join(result1) + ''.join(result2))
