a, b = map(int, input().split())

cnt = 1
while True:
    if b % 2 == 0:
        b //= 2
        cnt += 1
    else:
        if b % 10 == 1:
            b //= 10
            cnt += 1
        else:
            print(-1)
            exit()
    if a == b:
        print(cnt)
        exit()
    if a > b:
        print(-1)
        exit()
    