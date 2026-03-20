import time

def power_loop(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

def power_recursive(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        half = power_recursive(a, n // 2)
        return half * half
    else:
        return a * power_recursive(a, n - 1)

a, n = 2, 10000
start = time.time()
p1 = power_loop(a, n)
print(f"Цикл: {time.time() - start:.6f} сек")

start = time.time()
p2 = power_recursive(a, n)
print(f"Рекурсия: {time.time() - start:.6f} сек")
