def greet (name):
    return f'Привет, {name}!'


def square(number):
    return number**2


def max_of_two (x, y):
    return f'Наибольшее число: {max(x, y)}'


a = str(input('Введите имя:'))
print(greet(a))
b = int(input('Введите число, которое хотите возвести в квадрат:'))
print(square(b))
c = int(input('Введите первое число:'))
d = int(input('Введите второе число:'))
print(max_of_two(c, d))