import random

def random_multiply(n):
    if n == 0:
        return 1
    return n * random.randint(1, 10)

print(random_multiply(5))
