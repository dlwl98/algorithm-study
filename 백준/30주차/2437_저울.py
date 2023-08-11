import sys
input = sys.stdin.readline

n = int(input())
g = sorted(list(map(int, input().split())))

if g[0] != 1:
    print(1)
    exit()

tmp = 1
for i in range(1, len(g)):
    if g[i] > tmp + 1:
        print(tmp + 1)
        exit()
    tmp += g[i]

print(tmp + 1)
