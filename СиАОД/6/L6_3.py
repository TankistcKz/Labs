from L6_2 import SinglyLinkedList

class Stack:
    def __init__(self):
        self._list = SinglyLinkedList()

    def push(self, value):
        self._list.add_first(value)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self._list.get(0)
        self._list.remove_first()
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._list.get(0)

    def size(self):
        return self._list.size()

    def is_empty(self):
        return self.size() == 0


stack = Stack()
for val in [5, 0, 1, 7, 9]:
    stack.push(val)

print("Верхний элемент:", stack.peek())
stack.pop()
stack.pop()
print("Верхний элемент после удалений:", stack.peek())
print("Итоговый размер стека:", stack.size())
