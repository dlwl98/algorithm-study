from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = deque(input().rstrip())
cnt = 0

stack = []
while cnt < k:
    if len(stack) == 0:
        stack.append(nums.popleft())
        continue
    if len(nums) == 0 or int(stack[-1]) < int(nums[0]):
        stack.pop()
        cnt += 1
    else:
        stack.append(nums.popleft())


print(''.join(stack) + ''.join(nums))
