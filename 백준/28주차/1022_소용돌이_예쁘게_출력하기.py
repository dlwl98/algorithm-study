r1, c1, r2, c2 = map(int, input().split())

g = [[1] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
d = [[0, 1], [-1, 0], [0, -1], [1, 0]]

cur = [0, 0, 0, 2]
while True:
    y, x, di, cnt = cur
    if y >= 0 and y+1 == x:
        di = 1
    elif abs(y) == abs(x):
        if y < 0 or x < 0:
            di = (di + 1) % 4
    ny = y + d[di][0]
    nx = x + d[di][1]
    if ny == 5000 and nx == 5001:
        break
    if (r1 <= ny <= r2) and (c1 <= nx <= c2):
        g[ny - r1][nx - c1] = cnt
    cur = [ny, nx, di, cnt + 1]

tmp = 0
for a in g:
    tmp = max(tmp, max(a))

digit = len(str(tmp))

for a in g:
    for b in a:
        localDigit = len(str(b))
        for _ in range(digit - localDigit):
            print(' ', end='')
        print(b, end=' ')
    print()
