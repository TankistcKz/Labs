import time
import random
import numpy as np


"""Пользовательская реализация бинарного поиска."""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


N = 2_000_000
QUERIES = 1000

arr_list = sorted([random.randint(1, 10**7) for _ in range(N)])
arr_numpy = np.array(arr_list, dtype=np.int64)

# Цели: смесь существующих и отсутствующих
existing = random.sample(arr_list, QUERIES // 2)
missing = [-999999 for _ in range(QUERIES // 2)]
targets = existing + missing
random.shuffle(targets)

# 1. Собственная реализация (бинарный поиск на list)
start = time.perf_counter()
for t in targets:
    binary_search(arr_list, t)
t_custom = time.perf_counter() - start

# 2. list.index() — линейный поиск
start = time.perf_counter()
for t in targets:
    try:
        arr_list.index(t)
    except ValueError:
        pass
t_index = time.perf_counter() - start

# 3. Оператор in
start = time.perf_counter()
for t in targets:
    _ = t in arr_list
t_in = time.perf_counter() - start

# 4. numpy.searchsorted
start = time.perf_counter()
for t in targets:
    idx = np.searchsorted(arr_numpy, t)
    if idx < len(arr_numpy) and arr_numpy[idx] == t:
        pass
t_np = time.perf_counter() - start

print(f"{'Метод':<30} | {'Время (с)':<15}")
print(f"{'Пользовательский бинарный':<30} | {t_custom:<15.6f}")
print(f"{'list.index()':<30} | {t_index:<15.6f}")
print(f"{'operator in':<30} | {t_in:<15.6f}")
print(f"{'numpy.searchsorted':<30} | {t_np:<15.6f}")
