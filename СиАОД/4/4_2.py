import time
import math
import random
import matplotlib
import matplotlib.pyplot as plt

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

"""Равномерное распределение."""
def generate_uniform(size):
    return sorted([random.randint(1, 10**6) for _ in range(size)])

"""Квадратичное распределение (скученность в начале)."""
def generate_quadratic(size):
    return sorted([int((i / size) ** 2 * 10**6) for i in range(size)])

"""Экспоненциальное распределение."""
def generate_exponential(size):
    max_exp = math.log(10**6 + 1)
    return sorted([int(math.exp(i / size * max_exp)) for i in range(size)])

"""Случайные данные с перекосом."""
def generate_skewed(size):
    arr = [int(random.expovariate(0.001)) for _ in range(size)]
    return sorted(arr)


SIZE = 200000
QUERIES = 500
distributions = {
    "Равномерное": generate_uniform,
    "Квадратичное": generate_quadratic,
    "Экспоненциальное": generate_exponential,
    "Скошенное (exp)": generate_skewed,
}

results = []

for name, gen_func in distributions.items():
    arr = gen_func(SIZE)
    targets = random.sample(arr, QUERIES // 2) + [
        -999999 for _ in range(QUERIES // 2)
    ]

    # Интерполяционный
    start = time.perf_counter()
    for t in targets:
        interpolation_search(arr, t)
    t_interp = time.perf_counter() - start

    # Бинарный
    start = time.perf_counter()
    for t in targets:
        binary_search(arr, t)
    t_bin = time.perf_counter() - start
    results.append((name, t_interp, t_bin))

names = [r[0] for r in results]
ti_vals = [r[1] for r in results]
tb_vals = [r[2] for r in results]

x = range(len(names))
plt.figure(figsize=(10, 5))
width = 0.35
plt.bar([i - width/2 for i in x], ti_vals, width, label='Интерполяционный', color='skyblue')
plt.bar([i + width/2 for i in x], tb_vals, width, label='Бинарный', color='salmon')
plt.xticks(x, names, rotation=15)
plt.ylabel('Время (сек)')
matplotlib.use('Agg')
plt.title('Сравнение поисков на разных распределениях')
plt.legend()
plt.tight_layout()
plt.savefig('2.jpg', dpi=150)
