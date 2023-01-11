from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
visited = [False] * 200001


def bfs():
    queue = deque([[n, 0, []]])
    visited[n] = True
    while queue:
        cur, cnt, passed = queue.popleft()
        if cur == k:
            return [cnt, passed]
        for next_ in (cur - 1, cur + 1, cur * 2):
            if 0 <= next_ <= 100000 and not visited[next_]:
                queue.append([next_, cnt + 1, passed + [cur]])
                visited[next_] = True


def solution():
    if n == k:
        print(0)
        print(n)
        return
    if n > k:
        print(n - k)
        for i in range(n - k + 1):
            print(n - i, end=' ')
        return

    cnt, passed = bfs()
    print(cnt)
    print(*(passed + [k]))


solution()
