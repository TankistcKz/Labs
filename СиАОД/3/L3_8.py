def knapsack_3(capacities, items):
    cap1, cap2, cap3 = capacities
    n = len(items)
    
    dp = [[[[0]*(cap3+1) for _ in range(cap2+1)] for _ in range(cap1+1)] for _ in range(2)]
    decisions = [[[[None]*(cap3+1) for _ in range(cap2+1)] for _ in range(cap1+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        name, w, v = items[i-1]
        curr = i % 2
        prev = (i-1) % 2
        
        for c1 in range(cap1+1):
            for c2 in range(cap2+1):
                for c3 in range(cap3+1):
                    best = dp[prev][c1][c2][c3]
                    best_choice = (None, None)
                    
                    if c1 >= w and dp[prev][c1-w][c2][c3] + v > best:
                        best = dp[prev][c1-w][c2][c3] + v
                        best_choice = (1, w)
                    
                    if c2 >= w and dp[prev][c1][c2-w][c3] + v > best:
                        best = dp[prev][c1][c2-w][c3] + v
                        best_choice = (2, w)
                    
                    if c3 >= w and dp[prev][c1][c2][c3-w] + v > best:
                        best = dp[prev][c1][c2][c3-w] + v
                        best_choice = (3, w)
                    
                    dp[curr][c1][c2][c3] = best
                    decisions[i][c1][c2][c3] = best_choice


    c1, c2, c3 = cap1, cap2, cap3
    backpack1, backpack2, backpack3 = [], [], []
    total_value = dp[n%2][cap1][cap2][cap3]
    
    for i in range(n, 0, -1):
        choice = decisions[i][c1][c2][c3]
        if choice[0] is not None:
            name, w, v = items[i-1]
            if choice[0] == 1:
                backpack1.append(name)
                c1 -= w
            elif choice[0] == 2:
                backpack2.append(name)
                c2 -= w
            else:
                backpack3.append(name)
                c3 -= w
    
    return total_value, backpack1, backpack2, backpack3

with open('treasures.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    items = eval(content.split('=')[1].strip())

capacities = [10, 14, 18]
total, b1, b2, b3 = knapsack_3(capacities, items)

print(f"Максимальная суммарная стоимость: {total}")
print(f"\nРюкзак Пети (вместимость 10):")
for item in b1:
    print(f"  - {item}")
print(f"\nРюкзак Васи (вместимость 14):")
for item in b2:
    print(f"  - {item}")
print(f"\nРюкзак Терентия (вместимость 18):")
for item in b3:
    print(f"  - {item}")
print(f"\nВсего предметов: {len(b1) + len(b2) + len(b3)}")
