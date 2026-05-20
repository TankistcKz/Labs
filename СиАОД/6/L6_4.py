from L6_1 import DynamicArray
from L6_2 import SinglyLinkedList
import time

def test_structures(N):
    # Массив
    da = DynamicArray()
    start = time.perf_counter()
    for i in range(N):
        da.append(i)
    append_array = time.perf_counter() - start

    da = DynamicArray()
    for i in range(N):
        da.append(i)
    start = time.perf_counter()
    for _ in range(N):
        da.delete(0)
    delete_first_array = time.perf_counter() - start

    da = DynamicArray()
    for i in range(N):
        da.append(i)
    start = time.perf_counter()
    _ = da.get(N // 2)
    get_index_array = time.perf_counter() - start

    start = time.perf_counter()
    _ = da.size()
    size_array = time.perf_counter() - start

    # Список
    sll = SinglyLinkedList()
    start = time.perf_counter()
    for i in range(N):
        sll.add_last(i)
    append_list = time.perf_counter() - start

    sll = SinglyLinkedList()
    for i in range(N):
        sll.add_last(i)
    start = time.perf_counter()
    for _ in range(N):
        sll.remove_first()
    delete_first_list = time.perf_counter() - start

    sll = SinglyLinkedList()
    for i in range(N):
        sll.add_last(i)
    start = time.perf_counter()
    _ = sll.get(N // 2)
    get_index_list = time.perf_counter() - start

    start = time.perf_counter()
    _ = sll.size()
    size_list = time.perf_counter() - start

    return (append_array, delete_first_array, get_index_array, size_array), \
           (append_list, delete_first_list, get_index_list, size_list)

sizes = [100, 1000, 10000]

print(f"{'N':<8} {'Массив доб':<15} {'Список доб':<15} {'Массив удл':<15} {'Список удл':<15} {'Массив пол':<12} {'Список пол':<12} {'Массив разм':<12} {'Список разм':<12}")

for N in sizes:
    arr_res, lst_res = test_structures(N)
    print(f"{N:<8} {arr_res[0]:<15.6f} {lst_res[0]:<15.6f} {arr_res[1]:<15.6f} {lst_res[1]:<15.6f} {arr_res[2]:<12.6f} {lst_res[2]:<12.6f} {arr_res[3]:<12.6f} {lst_res[3]:<12.6f}")

