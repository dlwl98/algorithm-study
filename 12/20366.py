from itertools import combinations

n = int(input())
g = sorted(list(map(int, input().split())))

def two(s, e):
    arr = [10**9, 0, 0, 10**9]
    l = s + 1
    r = e - 1
    while l < r:
        tmp = g[s] + g[e] - g[l] - g[r]
        if abs(arr[0] + arr[3] - arr[1] - arr[2]) > abs(tmp):
            arr = [g[s], g[l], g[r], g[e]]
        if tmp == 0:
            return abs(arr[0] + arr[3] - arr[1] - arr[2])
        elif tmp < 0:
            r -= 1
        else:
            l += 1
    return abs(arr[0] + arr[3] - arr[1] - arr[2])

result = 10**9
for s, e in combinations(range(n), 2):
    result = min(result, two(s, e))

print(result)
