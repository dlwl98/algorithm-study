import math

N = int(input())
M = int(input())
buttons = [True] * 10
inputs = map(int, input().split()) if M != 0 else []
for idx in inputs:
    buttons[idx] = False


def check(number):
    str_number = str(number)
    for i in str_number:
        if not buttons[int(i)]:
            return False
    return True


def solution():
    result = min(int(1e9), abs(N - 100))
    for n in range(1000001):
        if check(n):
            result = min(result, abs(N - n) + len(str(n)))
    print(result)


solution()
