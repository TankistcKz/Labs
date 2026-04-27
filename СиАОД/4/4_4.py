import random


"""Возвращает (индекс, сравнения, итерации, сдвиги_указателя)."""
def modified_linear_search_stats(arr, target):
    comparisons = 0
    iterations = 0
    pointer_shifts = 0
    
    n = len(arr)
    if n == 0:
        return -1, 0, 0, 0

    last = arr[-1]
    arr[-1] = target
    i = 0
    while True:
        iterations += 1
        comparisons += 1
        if arr[i] == target:
            break
        i += 1
        pointer_shifts += 1

    arr[-1] = last
    if i < n - 1 or last == target:
        return i, comparisons, iterations, pointer_shifts
    return -1, comparisons, iterations, pointer_shifts

"""Возвращает (индекс, сравнения, итерации, изменения_границ)."""
def binary_search_stats(arr, target):
    comparisons = 0
    iterations = 0
    boundary_changes = 0
    
    left, right = 0, len(arr) - 1
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons, iterations, boundary_changes
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        boundary_changes += 1
    return -1, comparisons, iterations, boundary_changes

"""Возвращает (индекс, сравнения, итерации, изменения_границ)."""
def interpolation_search_stats(arr, target):
    comparisons = 0
    iterations = 0
    boundary_changes = 0
    
    low, high = 0, len(arr) - 1
    while low <= high:
        iterations += 1
        comparisons += 1
        if not (arr[low] <= target <= arr[high]):
            break
        if low == high:
            if arr[low] == target:
                return low, comparisons, iterations, boundary_changes
            break
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low, comparisons, iterations, boundary_changes
            break
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if pos < low or pos > high:
            break
        comparisons += 1
        if arr[pos] == target:
            return pos, comparisons, iterations, boundary_changes
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
        boundary_changes += 1
    return -1, comparisons, iterations, boundary_changes

"""Возвращает (индекс, сравнения, итерации, изменения_границ)."""
def exponential_search_stats(arr, target):
    comparisons = 0
    iterations = 0
    boundary_changes = 0
    
    n = len(arr)
    if n == 0:
        return -1, 0, 0, 0
    comparisons += 1
    if arr[0] == target:
        return 0, comparisons, iterations, boundary_changes

    i = 1
    while i < n:
        iterations += 1
        comparisons += 1
        if arr[i] > target:
            break
        if arr[i] == target:
            return i, comparisons, iterations, boundary_changes
        i *= 2
        boundary_changes += 1

    left = i // 2
    right = min(i, n - 1)
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons, iterations, boundary_changes
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        boundary_changes += 1
    return -1, comparisons, iterations, boundary_changes


SIZE = 1000
sorted_arr = sorted([random.randint(1, 10**6) for _ in range(SIZE)])
test_targets = [sorted_arr[0], sorted_arr[SIZE // 2], sorted_arr[-1], -999]
algorithms = {
    "Мод. линейный": (modified_linear_search_stats, True),
    "Бинарный": (binary_search_stats, False),
    "Интерполяционный": (interpolation_search_stats, False),
    "Экспоненциальный": (exponential_search_stats, False),
}
print(f"\n{'Алгоритм':<20} | {'Цель':<8} | {'Сравнения':<10} | {'Итерации':<10} | {'Сдвиги границ':<14} | {'Индекс':<8}")

for target in test_targets:
    for alg_name, (func, needs_copy) in algorithms.items():
        arr = sorted_arr[:] if needs_copy else sorted_arr
        idx, comps, iters, bounds = func(arr, target)
        print(f"{alg_name:<20} | {str(target):<8} | {comps:<10} | {iters:<10} | {bounds:<14} | {idx:<8}")
