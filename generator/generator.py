"""
Generator Functions

Generator functions are like normal functions, but one thing that is different
is that they use "yield" keyword to return something instead of the "return"
keyword. Also, instead of returning once, generator functions can yield multiple
times.

Generator functions also has the ability to keep track of its most recent state.

This is also a quick way of creating an iterator.
"""

def example(number):
    count = 0
    while count < number:
        yield count
        count += 1