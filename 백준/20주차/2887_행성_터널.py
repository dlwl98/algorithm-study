import sys
from heapq import heappop, heappush
from functools import cmp_to_key
input = sys.stdin.readline

def sx(a, b):
    return a[1] - b[1]
def sy(a, b):
    return a[2] - b[2]
def sz(a, b):
    return a[3] - b[3]

n = int(input())
g = [[i] + list(map(int, input().split())) for i in range(n)]
x = sorted(g, key=cmp_to_key(sx))
y = sorted(g, key=cmp_to_key(sy))
z = sorted(g, key=cmp_to_key(sz))
parent = [i for i in range(n)]

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

pq = []
for i in range(1, n):
    heappush(pq, [abs(x[i-1][1] - x[i][1]), x[i-1][0], x[i][0]])
    heappush(pq, [abs(y[i-1][2] - y[i][2]), y[i-1][0], y[i][0]])
    heappush(pq, [abs(z[i-1][3] - z[i][3]), z[i-1][0], z[i][0]])

cnt = 0
result = 0

while True:
    if cnt == n-1:
        break
    cost, a, b = heappop(pq)
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        result += cost

print(result)
