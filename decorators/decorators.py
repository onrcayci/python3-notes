"""
Decorators

Decorators are functions.

Decorators wrap other functions and enhance their behavior.

Decorators are examples of higher order functions

Decorators have their own syntax using "@".
"""

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Matt.")

greet()         # What a pleasure to meet you! My name is Matt. Have a great day!

# Functions with Different Signatures

def shout(fn):
    def wrapper(name):
        return fn(name).upper()
    return wrapper

@shout
def greeting(name):
    return f"Hi, I'm {name}"

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

print(greeting('todd'))         # HI, I'M TODD
print(order('burger', 'fries')) # ArgumentError

# Decorator Pattern

def shouting(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shouting
def greetings(name):
    return f"Hi, I'm {name}"

@shouting
def ordering(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

print(greetings("todd"))            # HI, I'm TODD
print(ordering("burger", "fries"))  # HI, I'D LIKE THE BURGER, WITH A SIDE OF FRIES, PLEASE.

# Preserving the metadata of a decorated function
from functools import wraps

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x, y):
    """Adds two number together."""
    return x + y

print(add.__doc__)  # Without @wraps, this will print out "I AM WRAPPER FUNCTION", with @wraps it prints out "Adds two numbers together"
print(add.__name__) # without @wraps -> wrapper, with @wraps -> add
help(add)           # without @wraps -> wrapper.__doc__, with @wraps -> add.__doc__