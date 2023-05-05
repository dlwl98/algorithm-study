n = int(input())
g = sorted(list(map(int, input().split())))

def solution(n, g):
    result = [10**9, 10**9, 10**9]
    for i in range(n):
        l = i+1
        r = n-1
        while l < r:
            if abs(sum(result)) > abs(g[i] + g[l] + g[r]):
                result = [g[i], g[l], g[r]]

            if g[i] + g[l] + g[r] == 0:
                return result
            elif g[i] + g[l] + g[r] > 0:
                r -= 1
            else:
                l += 1
    return result

print(*solution(n, g))