import time
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


"""Модифицированный линейный поиск с барьером."""
def modified_linear_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    last = arr[-1]
    arr[-1] = target
    i = 0
    while arr[i] != target:
        i += 1
    arr[-1] = last
    if i < n - 1 or last == target:
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

"""Интерполяционный поиск."""
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            return low if arr[low] == target else -1
        if arr[high] == arr[low]:
            return low if arr[low] == target else -1
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if pos < low or pos > high:
            break
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

"""Экспоненциальный поиск."""
def exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    left = i // 2
    right = min(i, n - 1)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


SIZES = [10**3, 10**4, 10**5, 10**6]
QUERIES_PER_SIZE = 200

algorithms = {
    "Модиф. линейный": (modified_linear_search, True),
    "Бинарный": (binary_search, False),
    "Интерполяционный": (interpolation_search, False),
    "Экспоненциальный": (exponential_search, False),
}

times = {name: [] for name in algorithms}

for N in SIZES:
    arr = sorted([random.randint(1, 10**7) for _ in range(N)])
    
    existing = random.sample(arr, QUERIES_PER_SIZE // 2)
    missing = [-999 for _ in range(QUERIES_PER_SIZE // 2)]
    targets = existing + missing

    for alg_name, (func, needs_copy) in algorithms.items():
        start = time.perf_counter()
        for t in targets:
            if needs_copy:
                func(arr[:], t)
            else:
                func(arr, t)
        elapsed = time.perf_counter() - start
        avg_time = elapsed / QUERIES_PER_SIZE
        times[alg_name].append(avg_time)

plt.figure(figsize=(12, 7))
markers = ['o', 's', '^', 'D']
for (alg_name, t_list), marker in zip(times.items(), markers):
    plt.plot(SIZES, t_list, marker=marker, label=alg_name, linewidth=2, markersize=8)

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Размер массива N')
plt.ylabel('Среднее время поиска (с)')
plt.title('Зависимость времени поиска от размера массива')
matplotlib.use('Agg')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('6.jpg', dpi=150)
