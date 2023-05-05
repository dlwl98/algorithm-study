from sys import stdin


def solution():
    t = int(input())
    for _ in range(t):
        a, b = map(int, stdin.readline().split())
        while a:
            x = (b - 1) // a + 1
            a = a * x - b
            b = b * x
        print(x)


solution()
