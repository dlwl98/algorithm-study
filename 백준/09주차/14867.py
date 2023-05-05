from collections import deque


def check_append(x, y, i, j):
    if (x, y) not in visited:
        visited[(x, y)] = visited[(i, j)] + 1
        q.append((x, y))


def solution():
    global visited, q
    a, b, c, d = map(int, input().split())
    visited = dict()

    q = deque()
    q.append((0, 0))
    visited[(0, 0)] = 0
    while q:
        i, j = q.popleft()
        if i == c and j == d:
            break
        if i != 0:
            check_append(0, j, i, j)
            if j != b:
                if i + j >= b:
                    check_append(i + j - b, b, i, j)
                else:
                    check_append(0, i + j, i, j)
        if j != 0:
            check_append(i, 0, i, j)
            if i != a:
                if i + j >= a:
                    check_append(a, i + j - a, i, j)
                else:
                    check_append(i + j, 0, i, j)
        if i != a:
            check_append(a, j, i, j)
        if j != b:
            check_append(i, b, i, j)

    print(visited[(c, d)] if (c, d) in visited else -1)


solution()
