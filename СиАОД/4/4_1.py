import numpy as np
import time
import random
import math
from typing import List, Tuple, Any
import matplotlib.pyplot as plt


"""Модифицированный линейный поиск с барьером.Возвращает индекс элемента или -1, если не найден."""
def modified_linear_search(arr: List, target: Any) -> int:
    n = len(arr)
    if n == 0:
        return -1
    # Барьер: временно добавляем искомый элемент в конец
    last = arr[-1]
    arr[-1] = target
    i = 0
    while arr[i] != target:
        i += 1
    # Восстанавливаем последний элемент
    arr[-1] = last
    if i < n - 1 or last == target:
        return i
    return -1

"""Бинарный поиск. Массив должен быть отсортирован по возрастанию."""
def binary_search(arr: List, target: Any) -> int:
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

"""Интерполяционный поиск. Массив должен быть отсортирован по возрастанию."""
def interpolation_search(arr: List, target: Any) -> int:
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            break
        # Формула интерполяции
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

"""Экспоненциальный поиск в отсортированном массиве."""
def exponential_search(arr: List, target: Any) -> int:
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    # Бинарный поиск на интервале [i//2, min(i, n-1)]
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
                

sorted_arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
unsorted_arr = [11, 3, 29, 7, 2, 17, 5, 13, 23, 19]

test_cases = [
    ("Присутствует (5)", sorted_arr, 5, True),
    ("Отсутствует (15)", sorted_arr, 15, True),
    ("Присутствует (11)", unsorted_arr, 11, False),
    ("Отсутствует (99)", unsorted_arr, 99, False),
]

for description, arr, target, is_sorted in test_cases:
    print(f"\nТест: {description} | Массив: {arr} | Искомое: {target}")
    arr_copy = arr[:]
    print(f"  Модифицированный линейный: {modified_linear_search(arr_copy, target)}")
    if is_sorted:
        print(f"  Бинарный: {binary_search(arr[:], target)}")
        print(f"  Интерполяционный: {interpolation_search(arr[:], target)}")
        print(f"  Экспоненциальный: {exponential_search(arr[:], target)}")
    else:
        print(f"  (Бинарный/интерпол./эксп. пропущены — массив не отсортирован)")
