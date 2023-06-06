while True:
    n = int(input())
    if n == 0:
        break
    tmp1 = 1
    tmp2 = 1
    for i in range(1, 2*n+1):
        tmp1 *= i
    for i in range(1, n+1):
        tmp2 *= i
    print(tmp1 // (tmp2 * tmp2) // (n+1))
