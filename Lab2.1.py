def greet(name):
    return f"Привет, {name}!"
 
def square(number):
    return number**2
    
    
def max_of_two(a, b):
    return max(a, b)
    
name = str(input("Введите ваше имя:"))
print(greet(name))
number = int(input("Введите число:"))
print(square(number))
a = int(input("Введите число:"))
b = int (input('Введите число:'))
print ('Наибольшее число:', max_of_two(a, b))

