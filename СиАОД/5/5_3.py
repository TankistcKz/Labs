import sys

"""
Рекурсивная сортировка слиянием.
Возвращает: (отсортированный_массив, сравнения, макс_глубина)
"""
def merge_sort_recursive(arr):
    a = arr[:]
    comparisons = [0]
    max_depth = [0]

    def merge_sort(left, right, depth):
        if depth > max_depth[0]:
            max_depth[0] = depth
        if left >= right:
            return
        mid = (left + right) // 2
        merge_sort(left, mid, depth + 1)
        merge_sort(mid + 1, right, depth + 1)
        merge(left, mid, right)

    def merge(left, mid, right):
        temp = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            comparisons[0] += 1
            if a[i] <= a[j]:
                temp.append(a[i])
                i += 1
            else:
                temp.append(a[j])
                j += 1
        while i <= mid:
            temp.append(a[i])
            i += 1
        while j <= right:
            temp.append(a[j])
            j += 1
        for k in range(len(temp)):
            a[left + k] = temp[k]

    merge_sort(0, len(a) - 1, 0)
    return a, comparisons[0], max_depth[0]

"""
Итерационная сортировка слиянием (восходящая).
Возвращает: (отсортированный_массив, сравнения, проходы)
"""
def merge_sort_iterative(arr):
    a = arr[:]
    n = len(a)
    comparisons = 0
    passes = 0
    width = 1
    while width < n:
        passes += 1
        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width - 1, n - 1)
            right = min(i + 2 * width - 1, n - 1)
            if mid < right:
                # Слияние a[left..mid] и a[mid+1..right]
                temp = []
                i1, i2 = left, mid + 1
                while i1 <= mid and i2 <= right:
                    comparisons += 1
                    if a[i1] <= a[i2]:
                        temp.append(a[i1])
                        i1 += 1
                    else:
                        temp.append(a[i2])
                        i2 += 1
                while i1 <= mid:
                    temp.append(a[i1])
                    i1 += 1
                while i2 <= right:
                    temp.append(a[i2])
                    i2 += 1
                for k in range(len(temp)):
                    a[left + k] = temp[k]
        width *= 2
    return a, comparisons, passes


cargo_priority = [
    42, 17, 93, 58, 11, 76, 24, 65, 39, 88, 5, 71, 30, 54, 19, 93, 7, 80,
    80, 48, 77, 98, 97, 56, 27, 94, 73, 74, 72, 47, 95, 70, 96, 93, 84, 53,
    38, 90, 94, 85, 34, 88, 56, 29, 65, 84, 72, 60, 63, 59, 61, 61, 14, 42,
    89, 97, 62, 27, 19, 36, 18, 89, 3, 64, 99, 38, 26, 99, 55, 40, 32, 99,
    86, 44, 1, 100, 53, 74, 78, 68, 21, 24, 85, 32, 99, 68, 85, 12, 4, 18,
    69, 46, 46, 50, 64, 7, 68, 27, 98, 77, 41, 76, 12, 12, 62, 75, 29, 52,
    12, 91, 73, 14, 22, 47, 47, 16, 25, 64, 54, 66, 89, 20, 68, 82, 4, 7,
    58, 42, 13, 3, 60, 10, 52, 25, 98, 64, 86, 48, 44, 38, 2, 33, 14, 28,
    29, 40, 23, 83, 47, 35
]

# Рекурсивная версия
sys.setrecursionlimit(2000)
sorted_rec, comps_rec, depth_rec = merge_sort_recursive(cargo_priority)
print(f"\nРекурсивная версия:")
print(f"  {sorted_rec}")
print(f"  Сравнений: {comps_rec}")
print(f"  Максимальная глубина рекурсии: {depth_rec}")

# Итерационная версия
sorted_iter, comps_iter, passes_iter = merge_sort_iterative(cargo_priority)
print(f"\nИтерационная версия:")
print(f"  {sorted_iter}")
print(f"  Сравнений: {comps_iter}")
print(f"  Число проходов: {passes_iter}")

print(f"\nПроверка: {sorted_rec == sorted_iter}")
