import sys
input = sys.stdin.readline

n, s = map(int, input().split())
g = list(map(int, input().split()))

start = 0
end = 0
result = n + 1
cur = g[0]
while start < n and end < n:
    if cur >= s:
        result = min(result, end - start + 1)
        cur -= g[start]
        start += 1
    else:
        end += 1
        if end >= n:
            break
        cur += g[end]

print(0 if result == n + 1 else result)
