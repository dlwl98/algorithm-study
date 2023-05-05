import sys
input = sys.stdin.readline

def in_range(y, x):
    return 0 <= y < 10 and  0 <= x < 10

def press(_g, y, x):
    for dy, dx in ((0, 0),(-1, 0),(0, 1),(1, 0),(0, -1)):
        ny, nx = y + dy, x + dx
        if in_range(ny, nx):
            _g[ny][nx] = (_g[ny][nx] + 1) % 2


g = [[0 for _ in range(10)] for _ in range(10)]
cases = [101] * (1 << 10)

for i in range(10):
    line = input().rstrip()
    for j in range(len(line)):
        if line[j] == "O":
            g[i][j] = 1

for case in range(len(cases)):
    _g = [g[i][:] for i in range(10)]

    cnt = 0
    mask = 1
    for j in range(9, -1, -1):
        if case & mask:
            press(_g, 0, j)
            cnt += 1
        mask <<= 1

    for i in range(1, 10):
        for j in range(10):
            if _g[i - 1][j]:
                press(_g, i, j)
                cnt += 1

    if sum(_g[9]) == 0:
        cases[case] = cnt

print(min(cases))
