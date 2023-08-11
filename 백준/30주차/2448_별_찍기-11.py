import sys
sys.setrecursionlimit(10**5)

n = int(input())
# 24 -> (0, 23) -> (0, 23), (12, 11), (12, 35)
result = [[' '] * (n*2) for _ in range(n)]
def go(y, x, size):
    if size != 3:
        go(y, x, size // 2)
        go(y + size // 2, x - size // 2, size // 2)
        go(y + size // 2, x + size // 2, size // 2)
    else:
        result[y][x] = '*'
        result[y+1][x-1] = '*'
        result[y+1][x+1] = '*'
        result[y+2][x-2] = '*'
        result[y+2][x-1] = '*'
        result[y+2][x] = '*'
        result[y+2][x+1] = '*'
        result[y+2][x+2] = '*'

go(0, n-1, n)
for line in result:
    for dot in line:
        print(dot, end='')
    print()
