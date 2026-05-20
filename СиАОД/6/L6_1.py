import ctypes

class DynamicArray:
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = value
        self._size += 1

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = value
        self._size += 1

    def delete(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        return self._array[index]

    def size(self):
        return self._size

    def __str__(self):
        return "[" + ", ".join(str(self.get(i)) for i in range(self._size)) + "]"


arr = DynamicArray()
for val in [5, 0, 1, 7, 9, 4, 6, 2, 1]:
    arr.append(val)

arr.insert(7, 8)
arr.delete(5)

print("Итоговый список:", arr)
print("Размер:", arr.size())
