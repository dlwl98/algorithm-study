import sys
input = sys.stdin.readline

n = int(input())
dp1 = [[0] * 3 for _ in range(2)]
dp2 = [[0] * 3 for _ in range(2)]

for i in range(n):
    a, b, c = map(int, input().split())
    if i == 0:
        dp1[0][0] = a
        dp1[0][1] = b
        dp1[0][2] = c
        dp2[0][0] = a
        dp2[0][1] = b
        dp2[0][2] = c
    else:
        for j in range(3):
            if j == 0:
                dp1[1][j] = a + max(dp1[0][0], dp1[0][1])
            if j == 1:
                dp1[1][j] = b + max(dp1[0])
            if j == 2:
                dp1[1][j] = c + max(dp1[0][1], dp1[0][2])
        dp1[0] = dp1[1][:]
        dp1[1] = [0, 0, 0]

        for j in range(3):
            if j == 0:
                dp2[1][j] = a + min(dp2[0][0], dp2[0][1])
            if j == 1:
                dp2[1][j] = b + min(dp2[0])
            if j == 2:
                dp2[1][j] = c + min(dp2[0][1], dp2[0][2])
        dp2[0] = dp2[1][:]
        dp2[1] = [0, 0, 0]

print(max(dp1[0]), min(dp2[0]))
