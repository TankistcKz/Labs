import copy

"""
Сортировка пузырьком.
Возвращает: (отсортированный_массив, сравнения, обмены, проходы)
"""
def bubble_sort(arr):
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
Сортировка выбором.
Возвращает: (отсортированный_массив, сравнения, обмены, проходы)
"""
def selection_sort(arr):
    a = arr[:]
    n = len(a)
    comparisons = 0
    swaps = 0
    passes = 0
    for i in range(n - 1):
        min_idx = i
        passes += 1
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return a, comparisons, swaps, passes

"""
Сортировка вставками.
Возвращает: (отсортированный_массив, сравнения, сдвиги, проходы)
"""
def insertion_sort(arr):
    a = arr[:]
    n = len(a)
    comparisons = 0
    shifts = 0
    passes = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        passes += 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
        if j + 1 != i:
            shifts += 1
    return a, comparisons, shifts, passes


data_random = [57, 12, 89, 34, 76, 11, 90, 43, 65, 28, 71, 5, 39, 84, 22]
data_sorted = [5, 11, 12, 22, 28, 34, 39, 43, 57, 65, 71, 76, 84, 89, 90]
data_reverse = [90, 89, 84, 76, 71, 65, 57, 43, 39, 34, 28, 22, 12, 11, 5]
data_almost = [5, 11, 12, 22, 28, 34, 43, 39, 57, 65, 71, 76, 84, 89, 90]

datasets = [
    ("Случайный", data_random),
    ("Отсортированный", data_sorted),
    ("Обратный", data_reverse),
    ("Почти отсортированный", data_almost),
]

algorithms = [
    ("Пузырьковая", bubble_sort),
    ("Выбором", selection_sort),
    ("Вставками", insertion_sort),
]


for data_name, data in datasets:
    print(50 * "=", data_name, 50 * "=")
    for alg_name, alg_func in algorithms:
        if alg_name == "Вставками":
            sorted_arr, comps, moves, passes = alg_func(data)
            print(f"\n{alg_name}:")
            print(f"  Отсортированный: {sorted_arr}")
            print(f"  Сравнений: {comps}, Сдвигов: {moves}, Проходов: {passes}")
        else:
            sorted_arr, comps, swaps, passes = alg_func(data)
            print(f"\n{alg_name}:")
            print(f"  Отсортированный: {sorted_arr}")
            print(f"  Сравнений: {comps}, Обменов: {swaps}, Проходов: {passes}")
