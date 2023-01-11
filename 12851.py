from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
visited = [int(1e9)] * 200001


def bfs():
    queue = deque([[n, 0]])
    visited[n] = True
    while queue:
        cur, cnt = queue.popleft()
        if cur == k:
            ways = 1
            while queue:
                cur_, cnt_ = queue.popleft()
                if cnt_ > cnt:
                    break
                if cur_ == k:
                    ways += 1
            return [cnt, ways]

        for next_ in (cur - 1, cur + 1, cur * 2):
            if 0 <= next_ <= 100000:
                if visited[next_] == int(1e9) or visited[next_] == cnt + 1:
                    queue.append([next_, cnt + 1])
                    visited[next_] = cnt + 1


def solution():
    if n == k:
        print(0)
        print(1)
        return
    if n > k:
        print(n - k)
        print(1)
        return

    cnt, ways = bfs()
    print(cnt)
    print(ways)


solution()
