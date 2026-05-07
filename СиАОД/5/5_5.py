"""Устойчивая пузырьковая сортировка (по ключу)."""
def bubble_sort_stable(arr):
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j][1] > a[j + 1][1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

"""Устойчивая сортировка вставками (по ключу)."""
def insertion_sort_stable(arr):    
    a = arr[:]
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j][1] > key[1]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

"""Неустойчивая сортировка выбором (по ключу)."""
def selection_sort_unstable(arr):
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][1] < a[min_idx][1]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a

"""Неустойчивая быстрая сортировка (Хоар, первый элемент)."""
def quicksort_hoare_unstable(arr):
    a = arr[:]

    def partition(low, high):
        pivot = a[low][1]
        i = low - 1
        j = high + 1
        while True:
            while True:
                i += 1
                if a[i][1] >= pivot:
                    break
            while True:
                j -= 1
                if a[j][1] <= pivot:
                    break
            if i >= j:
                return j
            a[i], a[j] = a[j], a[i]

    def sort(low, high):
        if low < high:
            p = partition(low, high)
            sort(low, p)
            sort(p + 1, high)

    sort(0, len(a) - 1)
    return a

"""
Проверка устойчивости: для каждого ключа сравниваем порядок
идентификаторов в исходном и отсортированном массивах.
"""
def check_stability(original, sorted_arr):
    from collections import defaultdict
    orig_order = defaultdict(list)
    for rec in original:
        orig_order[rec[1]].append(rec[0])

    sorted_order = defaultdict(list)
    for rec in sorted_arr:
        sorted_order[rec[1]].append(rec[0])

    for key in orig_order:
        if orig_order[key] != sorted_order[key]:
            return False
    return True


records1 = [
    ("A1", 4), ("A2", 2), ("A3", 4), ("A4", 1), ("A5", 3),
    ("A6", 2), ("A7", 4), ("A8", 1), ("A9", 3), ("A10", 2)
]

records2 = [
    ("B1", 5), ("B2", 5), ("B3", 5), ("B4", 2), ("B5", 2),
    ("B6", 3), ("B7", 3), ("B8", 3), ("B9", 1), ("B10", 1)
]

records3 = [
    ("C1", 3), ("C2", 1), ("C3", 3), ("C4", 2), ("C5", 3),
    ("C6", 1), ("C7", 2), ("C8", 3), ("C9", 1), ("C10", 2),
    ("C11", 3), ("C12", 1)
]

all_records = [
    (records1),
    (records2),
    (records3),
]

algorithms = [
    ("Пузырьковая", bubble_sort_stable, "устойчивая"),
    ("Вставками", insertion_sort_stable, "устойчивая"),
    ("Выбором", selection_sort_unstable, "неустойчивая"),
    ("Быстрая (Хоар)", quicksort_hoare_unstable, "неустойчивая"),
]


for records in all_records:
    print(f"\n{'═' * 50}")
    print(f"Исходный: {records}")

    for alg_name, alg_func, expected in algorithms:
        sorted_records = alg_func(records)
        is_stable = check_stability(records, sorted_records)
        status = "УСТОЙЧИВ" if is_stable else "НЕУСТОЙЧИВ"
        print(f"\n{alg_name} ({expected}):")
        print(f"  Результат: {sorted_records}")
        print(f"  Статус: {status}")

print("Шаг 1: сортировка по идентификатору (все алгоритмы)")
print("Шаг 2: сортировка по ключу устойчивым и неустойчивым алгоритмом")

demo = records3[:]
demo_sorted_by_id = sorted(demo, key=lambda x: x[0])
print(f"\nПосле сортировки по ID: {demo_sorted_by_id}")

result_stable = insertion_sort_stable(demo_sorted_by_id)
print(f"После устойчивой сортировки по ключу: {result_stable}")

result_unstable = quicksort_hoare_unstable(demo_sorted_by_id)
print(f"После неустойчивой сортировки по ключу: {result_unstable}")

print(f"\nУстойчивый алгоритм сохранил порядок ID при равных ключах: "
      f"{check_stability(demo_sorted_by_id, result_stable)}")
print(f"Неустойчивый алгоритм сохранил порядок ID при равных ключах: "
      f"{check_stability(demo_sorted_by_id, result_unstable)}")
