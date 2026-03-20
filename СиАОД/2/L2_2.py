import time

def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

test_values = [10, 100, 500, 1000]
for n in test_values:
    start = time.time()
    fact_loop = factorial_loop(n)
    loop_time = time.time() - start
    
    start = time.time()
    fact_rec = factorial_recursive(n)
    rec_time = time.time() - start
    
    print(f"n = {n}: Цикл = {loop_time:.6f} сек, Рекурсия = {rec_time:.6f} сек")
