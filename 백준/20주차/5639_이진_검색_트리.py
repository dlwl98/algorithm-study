import sys
sys.setrecursionlimit(10 ** 5)

nodes = list(map(int, sys.stdin.readlines()))

def go(start, end):
    if start > end:
        return

    i = start + 1
    while i <= end:
        if nodes[i] > nodes[start]:
            break
        i += 1

    go(start + 1, i - 1)
    go(i, end)
    print(nodes[start])

go(0, len(nodes) - 1)
