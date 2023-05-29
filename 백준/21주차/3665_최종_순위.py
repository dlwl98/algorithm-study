import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    past = list(map(int, input().split()))
    m = int(input())
    datas = [list(map(int, input().split())) for _ in range(m)]

    cnt = [0] * (n+1)
    for i in range(1, n+1):
        cnt[past[i-1]] = i-1

    g = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        g[past[i-1]] = set(past[i:])

    for a, b in datas:
        if a in g[b]:
            g[b].discard(a)
            cnt[a] -= 1
            g[a].add(b)
            cnt[b] += 1
        else:
            g[a].discard(b)
            cnt[b] -= 1
            g[b].add(a)
            cnt[a] += 1

    result = {}
    for i in range(1, n+1):
        if cnt[i] < 0:
            print("?")
            return
        if cnt[i] in result:
            print("IMPOSSIBLE")
            return
        result[cnt[i]] = i
    
    for i in range(n):
        print(result[i], end=' ')


t = int(input())
for _ in range(t):
    solution()
