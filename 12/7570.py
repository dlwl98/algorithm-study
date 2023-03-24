import heapq

n = int(input())
g = list(map(int, input().split()))
idx = [-1] * 1000001
for i in range(n):
    idx[g[i]] = i

tmp = idx[1]
arr = [1]
arr2 = []
for i in range(2, n+1):
    if idx[i] < tmp:
        heapq.heappush(arr2, -len(arr))
        arr = [i]
    else:
        arr.append(i)
    tmp = idx[i]
heapq.heappush(arr2, -len(arr))

result = heapq.heappop(arr2)
print(n + result)
