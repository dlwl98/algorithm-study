from sys import stdin
from bisect import bisect_left, bisect_right

order = int(stdin.readline())
A_len, B_len = map(int, stdin.readline().split())
A, B = [], []
for _ in range(A_len):
    A.append(int(stdin.readline()))
for _ in range(B_len):
    B.append(int(stdin.readline()))


def solution():
    result = 0
    ap = [0, sum(A)]
    bp = [0, sum(B)]
    for i in range(A_len):
        tmp = 0
        for j in range(A_len-1):
            tmp += A[i+j] if i+j < A_len else A[i+j-A_len]
            if tmp > order:
                continue
            ap.append(tmp)

    for i in range(B_len):
        tmp = 0
        for j in range(B_len-1):
            tmp += B[i+j] if i+j < B_len else B[i+j-B_len]
            if tmp > order:
                continue
            bp.append(tmp)

    ap.sort()
    bp.sort()

    for i in ap:
        target = order - i
        left = bisect_left(bp, target)
        right = bisect_right(bp, target)
        result += right - left

    print(result)


solution()
