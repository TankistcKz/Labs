def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, int(number**0.5)+1))
    
    
number = int(input('Введите число:'))
print(is_prime(number))