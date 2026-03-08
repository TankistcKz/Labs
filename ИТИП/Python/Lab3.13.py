f = input('Введите имя файла: \n')+'.txt'
try:
    file = open(f)
except FileNotFoundError:
    print (f'Файл "{f}" не найден.')
    exit()

r = str(input('Вывести файл построчно? \n'))
if r.lower() == 'да':
    print('\n')
    for line in file:
        print(line)
else: print('\n', file.read())
file.close()