import random
import sys

sys.setrecursionlimit(5000)

"""
Быстрая сортировка (схема Хоара).
pivot_choice: 'first', 'middle', 'random'
Возвращает: (отсортированный_массив, сравнения, обмены, вызовы_разбиения, макс_глубина, шаги)
"""
def quicksort_hoare(arr, pivot_choice='first'):
    a = arr[:]
    comparisons = [0]
    swaps = [0]
    partition_calls = [0]
    max_depth = [0]
    steps_log = []

    def choose_pivot(low, high):
        if pivot_choice == 'first':
            return low
        elif pivot_choice == 'middle':
            return (low + high) // 2
        elif pivot_choice == 'random':
            return random.randint(low, high)
        return low

    def partition(low, high):
        partition_calls[0] += 1
        pivot_idx = choose_pivot(low, high)
        pivot = a[pivot_idx]
        # Меняем опорный с первым элементом
        if pivot_idx != low:
            a[low], a[pivot_idx] = a[pivot_idx], a[low]
            swaps[0] += 1
        i = low - 1
        j = high + 1
        while True:
            while True:
                i += 1
                comparisons[0] += 1
                if a[i] >= pivot:
                    break
            while True:
                j -= 1
                comparisons[0] += 1
                if a[j] <= pivot:
                    break
            if i >= j:
                # Логируем первые 3 разбиения
                if partition_calls[0] <= 3:
                    steps_log.append({
                        'call': partition_calls[0],
                        'low': low, 'high': high,
                        'pivot': pivot,
                        'array_state': a[:],
                        'return_j': j
                    })
                return j
            a[i], a[j] = a[j], a[i]
            swaps[0] += 1

    def sort(low, high, depth):
        if depth > max_depth[0]:
            max_depth[0] = depth
        if low < high:
            p = partition(low, high)
            sort(low, p, depth + 1)
            sort(p + 1, high, depth + 1)

    sort(0, len(a) - 1, 0)
    return a, comparisons[0], swaps[0], partition_calls[0], max_depth[0], steps_log

"""
Быстрая сортировка (схема Ломуто).
pivot_choice: 'last', 'middle', 'random'
Возвращает: (отсортированный_массив, сравнения, обмены, вызовы_разбиения, макс_глубина, шаги)
"""
def quicksort_lomuto(arr, pivot_choice='last'):
    a = arr[:]
    comparisons = [0]
    swaps = [0]
    partition_calls = [0]
    max_depth = [0]
    steps_log = []

    def choose_pivot(low, high):
        if pivot_choice == 'last':
            return high
        elif pivot_choice == 'middle':
            return (low + high) // 2
        elif pivot_choice == 'random':
            return random.randint(low, high)
        return high

    def partition(low, high):
        partition_calls[0] += 1
        pivot_idx = choose_pivot(low, high)
        pivot = a[pivot_idx]
        # Меняем опорный с последним элементом
        if pivot_idx != high:
            a[high], a[pivot_idx] = a[pivot_idx], a[high]
            swaps[0] += 1
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                swaps[0] += 1
        a[i + 1], a[high] = a[high], a[i + 1]
        swaps[0] += 1

        if partition_calls[0] <= 3:
            steps_log.append({
                'call': partition_calls[0],
                'low': low, 'high': high,
                'pivot': pivot,
                'array_state': a[:],
                'return_idx': i + 1
            })
        return i + 1

    def sort(low, high, depth):
        if depth > max_depth[0]:
            max_depth[0] = depth
        if low < high:
            p = partition(low, high)
            sort(low, p - 1, depth + 1)
            sort(p + 1, high, depth + 1)

    sort(0, len(a) - 1, 0)
    return a, comparisons[0], swaps[0], partition_calls[0], max_depth[0], steps_log


orders_random = [
    57, 14, 83, 29, 61, 45, 72, 10, 34, 98, 21, 66, 39, 50, 7, 66, 28, 64,
    72, 62, 66, 26, 8, 29, 89, 35, 15, 32, 27, 55, 3, 59, 100, 21, 56, 85,
    36, 23, 75, 18, 49, 18, 78, 44, 59, 59, 96, 68, 23, 81, 89, 4, 25, 90,
    92, 72, 8, 82, 89, 44, 82, 55, 49, 23, 49, 80, 22, 84, 67, 21, 88, 65,
    73, 99, 88, 49, 92, 39, 83, 66, 83, 26, 53, 75, 56, 94, 59, 89, 71, 37,
    64, 99, 96, 73, 83, 30, 79, 78, 29, 7
]

orders_duplicates = [
    5, 3, 5, 2, 5, 1, 5, 4, 5, 0, 5, 3, 5, 2, 5, 1, 9, 7, 0, 10, 4, 8, 2,
    6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 3, 6, 10, 5, 1, 9, 4, 0, 7, 2, 8, 6,
    3, 10, 5, 1, 9, 0, 4, 7, 8, 2, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 6, 3,
    10, 5, 1, 9, 0, 4, 7, 2, 8, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 6, 3, 10,
    5, 1, 9, 0, 4, 7, 2, 8
]

datasets = [
    ("orders_random", orders_random),
    ("orders_many_duplicates", orders_duplicates),
]

schemes = [
    ("Хоар", quicksort_hoare, ['first', 'middle', 'random']),
    ("Ломуто", quicksort_lomuto, ['last', 'middle', 'random']),
]


random.seed(42)

for data_name, data in datasets:
    print(f"Массив: {data_name}", 50 * "=")

    for scheme_name, scheme_func, pivot_modes in schemes:
        for pivot_mode in pivot_modes:
            result, comps, sw, calls, depth, steps = scheme_func(data, pivot_mode)
            print(f"\n{scheme_name} / опорный={pivot_mode}:")
            print(f"  Сравнений: {comps}, Обменов: {sw}")
            print(f"  Вызовов разбиения: {calls}, Макс. глубина: {depth}")
            print(f"  Первые 3 разбиения:")
            for step in steps:
                if scheme_name == "Хоар":
                    print(f"    Вызов {step['call']}: low={step['low']}, high={step['high']}, "
                          f"pivot={step['pivot']}, возврат j={step['return_j']}")
                else:
                    print(f"    Вызов {step['call']}: low={step['low']}, high={step['high']}, "
                          f"pivot={step['pivot']}, возврат idx={step['return_idx']}")


print("orders_random:")
print(f"{'Схема':<8} {'Опорный':<10} {'Сравнений':<12} {'Обменов':<10} {'Вызовов':<10} {'Глубина':<10}")

for scheme_name, scheme_func, pivot_modes in schemes:
    for pivot_mode in pivot_modes:
        result, comps, sw, calls, depth, _ = scheme_func(orders_random, pivot_mode)
        print(f"{scheme_name:<8} {pivot_mode:<10} {comps:<12} {sw:<10} {calls:<10} {depth:<10}")


print("orders_many_duplicates:")
print(f"{'Схема':<8} {'Опорный':<10} {'Сравнений':<12} {'Обменов':<10} {'Вызовов':<10} {'Глубина':<10}")

for scheme_name, scheme_func, pivot_modes in schemes:
    for pivot_mode in pivot_modes:
        result, comps, sw, calls, depth, _ = scheme_func(orders_duplicates, pivot_mode)
        print(f"{scheme_name:<8} {pivot_mode:<10} {comps:<12} {sw:<10} {calls:<10} {depth:<10}")
