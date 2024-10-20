i=1
file = open('user_input.txt', 'a')
a = input('Запись файла:\n')
file.write(f'{a}\n')
while i != 0:
    b = input()
    if b == '':
        i = 0
        break
    file.write(f'{b}\n')
file.close()