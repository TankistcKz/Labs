import time
import matplotlib.pyplot as plt
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

sizes = [100, 200, 400, 800, 1600, 3200]
repeats = 5
avg_times = []

for n in sizes:
    total_time = 0
    for _ in range(repeats):
        data = [random.randint(0, 10000) for _ in range(n)]
        start = time.perf_counter()
        bubble_sort(data.copy())
        end = time.perf_counter()
        total_time += (end - start)
    avg_time = total_time / repeats
    avg_times.append(avg_time)
    print(f"n = {n}, среднее время = {avg_time:.6f} сек")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(sizes, avg_times, marker='o')
plt.title('Зависимость времени от n')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (сек)')
plt.grid(True)

n_squared = [n**2 for n in sizes]
plt.subplot(1, 2, 2)
plt.plot(n_squared, avg_times, marker='o', color='orange')
plt.title('Зависимость времени от n²')
plt.xlabel('n²')
plt.ylabel('Время (сек)')
plt.grid(True)

plt.tight_layout()
plt.show()