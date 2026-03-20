import time
import matplotlib.pyplot as plt
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sizes = [1000, 2000, 5000, 10000]
bubble_times = []
sort_times = []

for n in sizes:
    data = [random.randint(0, 100000) for _ in range(n)]

    start = time.perf_counter()
    bubble_sort(data.copy())
    end = time.perf_counter()
    bubble_times.append(end - start)

    start = time.perf_counter()
    sorted(data.copy())
    end = time.perf_counter()
    sort_times.append(end - start)

    print(f"n = {n}: Bubble = {bubble_times[-1]:.4f} сек, sorted() = {sort_times[-1]:.6f} сек")

plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_times, marker='o', label='Пузырьковая (O(n²))')
plt.plot(sizes, sort_times, marker='s', label='Встроенная sorted() (O(n log n))')
plt.title('Сравнение времени выполнения сортировок')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (сек)')
plt.legend()
plt.grid(True)
plt.show()