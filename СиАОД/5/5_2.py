"""Базовая пузырьковая сортировка со статистикой."""
def bubble_sort_stats(arr):
    a = arr[:]
    n = len(a)
    comparisons = 0
    swaps = 0
    passes = 0
    for i in range(n - 1):
        swapped = False
        passes += 1
        for j in range(n - 1 - i):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return a, comparisons, swaps, passes

"""
Шейкерная сортировка (перемешиванием).
Возвращает: (отсортированный_массив, сравнения, обмены, проходы)
"""
def shaker_sort(arr):
    a = arr[:]
    n = len(a)
    comparisons = 0
    swaps = 0
    passes = 0
    left = 0
    right = n - 1
    while left < right:
        swapped = False
        passes += 1
        for i in range(left, right):
            comparisons += 1
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swaps += 1
                swapped = True
        right -= 1
        if not swapped:
            break

        swapped = False
        passes += 1
        for i in range(right, left, -1):
            comparisons += 1
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                swaps += 1
                swapped = True
        left += 1
        if not swapped:
            break
    return a, comparisons, swaps, passes

"""
Гномья сортировка.
Возвращает: (отсортированный_массив, сравнения, перестановки, шаги)
"""
def gnome_sort(arr):
    a = arr[:]
    n = len(a)
    comparisons = 0
    swaps = 0
    steps = 0
    i = 0
    while i < n:
        steps += 1
        if i == 0:
            i += 1
        else:
            comparisons += 1
            if a[i] >= a[i - 1]:
                i += 1
            else:
                a[i], a[i - 1] = a[i - 1], a[i]
                swaps += 1
                i -= 1
    return a, comparisons, swaps, steps


data1 = [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]
data2 = [2, 1, 3, 4, 5, 6, 7, 8, 10, 9]
data3 = [1, 3, 2, 4, 5, 7, 6, 8, 10, 9]
data4 = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

datasets = [
    ("data1 [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]", data1),
    ("data2 [2, 1, 3, 4, 5, 6, 7, 8, 10, 9]", data2),
    ("data3 [1, 3, 2, 4, 5, 7, 6, 8, 10, 9]", data3),
    ("data4 [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]", data4),
]

algorithms = [
    ("Пузырьковая", bubble_sort_stats),
    ("Шейкерная", shaker_sort),
    ("Гномья", gnome_sort),
]

for data_name, data in datasets:
    print(f"Массив: {data_name}", 50 * "=")

    for alg_name, alg_func in algorithms:
        if alg_name == "Гномья":
            sorted_arr, comps, swaps, steps = alg_func(data)
            print(f"\n{alg_name}:")
            print(f"  Результат: {sorted_arr}")
            print(f"  Сравнений: {comps}, Перестановок: {swaps}, Шагов: {steps}")
        else:
            sorted_arr, comps, swaps, passes = alg_func(data)
            print(f"\n{alg_name}:")
            print(f"  Результат: {sorted_arr}")
            print(f"  Сравнений: {comps}, Обменов: {swaps}, Проходов: {passes}")
