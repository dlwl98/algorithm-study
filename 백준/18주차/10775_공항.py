import sys
input = sys.stdin.readline

def check(arr):
    for i in range(len(arr)):
        if i >= tmp[i]:
            return False
    return True

n = int(input())
p = int(input())
g = [int(input()) for i in range(p)]

s = 1
e = p + 1
while s != e:
    mid = (s + e) // 2
    tmp = g[:mid]
    tmp.sort()
    if check(tmp):
        s = mid + 1
    else:
        e = mid

print(s - 1)
