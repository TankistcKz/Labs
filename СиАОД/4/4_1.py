def linear_search_barrier(arr, target):
    arr.append(target)  # барьер
    i = 0
    comparisons = 0
    iterations = 0
    shifts = 0
    while arr[i] != target:
        comparisons += 1
        i += 1
        iterations += 1
        shifts += 1
    arr.pop()
    if i == len(arr):
        return -1, comparisons, iterations, shifts
    return i, comparisons, iterations, shifts
    

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    iterations = 0
    shifts = 0
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        shifts += 1
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons, iterations, shifts
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        shifts += 1
    return -1, comparisons, iterations, shifts
    

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0
    iterations = 0
    shifts = 0
    while low <= high and arr[low] <= target <= arr[high]:
        iterations += 1
        if arr[high] == arr[low]:
            pos = low
        else:
            pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        shifts += 1
        comparisons += 1
        if arr[pos] == target:
            return pos, comparisons, iterations, shifts
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
        shifts += 1
    return -1, comparisons, iterations, shifts
    

def exponential_search(arr, target):
    if arr[0] == target:
        return 0, 1, 1, 0
    i = 1
    comparisons = 1
    iterations = 0
    shifts = 0
    while i < len(arr) and arr[i] <= target:
        comparisons += 1
        i *= 2
        iterations += 1
        shifts += 1
    left, right = i // 2, min(i, len(arr) - 1)
    res, c, it, sh = binary_search(arr[left:right+1], target)
    if res != -1:
        return left + res, comparisons + c, iterations + it, shifts + sh
    return -1, comparisons + c, iterations + it, shifts + sh
    

test_cases = [
    ([1, 3, 5, 7, 9], 5),
    ([1, 3, 5, 7, 9], 2),
    ([10, 20, 30, 40, 50], 10),
    ([10, 20, 30, 40, 50], 50),
    ([10, 20, 30, 40, 50], 100),
    ([5], 5),
    ([5], 3)
]

print("=" * 80)
print("ТЕСТИРОВАНИЕ МОДИФИЦИРОВАННОГО ЛИНЕЙНОГО ПОИСКА")
print("=" * 80)
for arr, target in test_cases:
    result = linear_search_barrier(arr.copy(), target)
    print(f"Массив: {arr}, Искомое: {target} -> Индекс: {result}")

print("\n" + "=" * 80)
print("ТЕСТИРОВАНИЕ БИНАРНОГО ПОИСКА")
print("=" * 80)
for arr, target in test_cases:
    result = binary_search(arr, target)
    print(f"Массив: {arr}, Искомое: {target} -> Индекс: {result}")

print("\n" + "=" * 80)
print("ТЕСТИРОВАНИЕ ИНТЕРПОЛЯЦИОННОГО ПОИСКА")
print("=" * 80)
for arr, target in test_cases:
    result = interpolation_search(arr, target)
    print(f"Массив: {arr}, Искомое: {target} -> Индекс: {result}")

print("\n" + "=" * 80)
print("ТЕСТИРОВАНИЕ ЭКСПОНЕНЦИАЛЬНОГО ПОИСКА")
print("=" * 80)
for arr, target in test_cases:
    result = exponential_search(arr, target)
    print(f"Массив: {arr}, Искомое: {target} -> Индекс: {result}")

print("\n" + "=" * 80)
print("СРАВНЕНИЕ РЕЗУЛЬТАТОВ ВСЕХ АЛГОРИТМОВ")
print("=" * 80)
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
targets = [4, 12, 20, 1, 15]

print(f"Отсортированный массив: {arr}\n")
print(f"{'Элемент':<15}{'Linear':<15}{'Binary':<15}{'Interpolation':<15}{'Exponential':<15}")
print("-" * 75)
for target in targets:
    r1 = linear_search_barrier(arr.copy(), target)
    r2 = binary_search(arr, target)
    r3 = interpolation_search(arr, target)
    r4 = exponential_search(arr, target)
    print(f"{target:<15}{r1:<15}{r2:<15}{r3:<15}{r4:<15}")
