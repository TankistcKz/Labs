def discribe_person(name, age=30):
    return f'Имя: {name}, {age} лет'
    
    
name = str(input('Введите своё имя:'))
age = input('Введите ваш возраст:')
if age.isdigit() == True:
    print(discribe_person(name, age))
else: print(discribe_person(name))