n = int(input())
s = []
w = []
for _ in range(n):
    _s, _w = map(int, input().split())
    s.append(_s)
    w.append(_w)

result = 0
def dfs(i, cnt):
    global result
    result = max(result, cnt)
    if i >= n:
        return

    if s[i] <= 0:
        dfs(i+1, cnt)
    else:
        for j in range(n):
            if i == j:
                continue
            if s[j] > 0:
                tmp = 0
                s[j] -= w[i]
                s[i] -= w[j]
                if s[j] <= 0:
                    tmp += 1
                if s[i] <= 0:
                    tmp += 1
                dfs(i+1, cnt + tmp)
                s[j] += w[i]
                s[i] += w[j]

dfs(0, 0)
print(result)
