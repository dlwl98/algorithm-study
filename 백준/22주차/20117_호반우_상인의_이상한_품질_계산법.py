import sys
input = sys.stdin.readline

n = int(input())
g = sorted(list(map(int, input().split())))

for i in range(n // 2):
    g[i] = g[n-i-1]

print(sum(g))
