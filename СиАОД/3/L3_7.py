def greedy_change(amount, coins):
    coins.sort(reverse=True)
    res = []
    for c in coins:
        while amount >= c:
            res.append(c)
            amount -= c
    return res

def dp_change(amount, coins):
    INF = 10**9
    dp = [INF]*(amount+1)
    dp[0] = 0
    used = [[] for _ in range(amount+1)]
    for x in range(1, amount+1):
        for c in coins:
            if x >= c and dp[x-c] + 1 < dp[x]:
                dp[x] = dp[x-c] + 1
                used[x] = used[x-c] + [c]
    return used[amount] if dp[amount] != INF else None

coins1 = [1, 5, 10, 25, 50, 100]
coins2 = [1, 4, 6, 9]
amounts = [23, 37, 58, 74, 99, 123]

for coins in [coins1, coins2]:
    for amount in amounts:
        g = greedy_change(amount, coins)
        d = dp_change(amount, coins)
        print(f"Сумма {amount}, номиналы {coins}")
        print(f"Жадный: {len(g)} монет, {g}")
        print(f"DP: {len(d)} монет, {d}")
        print("Совпадают" if sorted(g) == sorted(d) else "Не совпадают")
        print()
