def solution():
    inputs = input().split()
    n, m = int(inputs[0]), int(''.join(inputs[1].split('.')))
    cals = []
    prices = []
    for _ in range(n):
        inputs = input().split()
        cals.append(int(inputs[0]))
        prices.append(int(''.join(inputs[1].split('.'))))

    if cals and prices:
        dp = [0] * (m + 1)

        for i in range(n):
            for j in range(1, m + 1):
                if prices[i] <= j:
                    dp[j] = max(dp[j], dp[j - prices[i]] + cals[i])

        print(dp[m])
        solution()


solution()
