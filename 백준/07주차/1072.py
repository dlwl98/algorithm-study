X, Y = map(int, input().split())


def solution():
    per = int(Y * 100 / X)
    if per >= 99:
        print(-1)
    else:
        start = 1
        end = 1000000000
        while start <= end:
            mid = (start + end) // 2
            tmp = int((Y + mid) * 100 / (X + mid))
            if tmp > per:
                end = mid - 1
            else:
                start = mid + 1

        print(start)


solution()
