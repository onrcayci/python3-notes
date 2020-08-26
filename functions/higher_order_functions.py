"""
Higher Order Functions

We can pass functions as arguments to other functions.

We can also nest function inside one another.

We can also return functions from other functions.
"""

from random import choice

def sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total

def square(x):
    return x * x

def cube(x):
    return x ** 3

print(sum(3, square))   # 14 (1 + 4 + 9)
print(sum(3, cube))     # 36 (1 + 8 + 27)

# Nesting functions and running a function inside of another function
def greet(person):
    def get_mood():
        msg = choice(('Hello there ', 'Go away ', 'I love you '))
        return msg
    
    result = get_mood() + person
    return result

# Returning a function as a result of another function
def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHAH', 'lol', 'tehehe'))
        return l
    
    return get_laugh

# Inner functions can access outer function scope
def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHAHAH', 'lol', 'tehehe'))
        return f'{laugh} {person}'
    
    return get_laugh