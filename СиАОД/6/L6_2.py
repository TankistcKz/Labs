class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def add_last(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def remove_first(self):
        if not self.head:
            raise Exception("Empty list")
        self.head = self.head.next
        self._size -= 1

    def remove_last(self):
        if not self.head:
            raise Exception("Empty list")
        if not self.head.next:
            self.head = None
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None
        self._size -= 1

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.value

    def size(self):
        return self._size

    def __str__(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        return "[" + ", ".join(values) + "]"


lst = SinglyLinkedList()
for val in [5, 3, 5, 20]:
    lst.add_last(val)

lst.add_last(7)
lst.remove_first()
lst.remove_last()

print("Итоговый список:", lst)
print("Размер:", lst.size())
