import time
import random
import matplotlib
import matplotlib.pyplot as plt

"""Простой линейный поиск."""
def linear_search_all(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

"""Бинарный поиск."""
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


N = 50000
K_values = [1, 5, 10, 25, 50, 100, 250, 500, 1000, 2000, 5000]
   
arr_original = [random.randint(1, 10**6) for _ in range(N)]
all_targets = [random.choice(arr_original) for _ in range(max(K_values))]

linear_times = []
sort_binary_times = []

for K in K_values:
    targets = all_targets[:K]
    # Подход 1: линейный поиск K раз
    start = time.perf_counter()
    for t in targets:
        linear_search_all(arr_original, t)
    t_linear = time.perf_counter() - start
    linear_times.append(t_linear)

    # Подход 2: сортировка + K бинарных поисков
    start = time.perf_counter()
    sorted_arr = sorted(arr_original)
    for t in targets:
        binary_search(sorted_arr, t)
    t_sort_bin = time.perf_counter() - start
    sort_binary_times.append(t_sort_bin)

plt.figure(figsize=(10, 6))
plt.plot(K_values, linear_times, 'o-', label='Linear total', linewidth=2)
plt.plot(K_values, sort_binary_times, 's-', label='Sort + Binary total', linewidth=2)
plt.xlabel('Число запросов K')
plt.ylabel('Общее время (сек)')
plt.title(f'Порог выгодности сортировки (N={N})')
matplotlib.use('Agg')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('3.jpg', dpi=150)
