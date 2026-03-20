import os

file_path = "text.txt"

with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    def count_spaces_loop(s):
        count = 0
        for char in s:
            if char == ' ':
                count += 1
        return count

    def count_spaces_recursive(s):
        if not s:
            return 0
        return (1 if s[0] == ' ' else 0) + count_spaces_recursive(s[1:])

    loop_count = count_spaces_loop(text)
    recursive_count = count_spaces_recursive(text)

    print(f"Циклическая реализация: {loop_count}")
    print(f"Рекурсивная реализация: {recursive_count}")
