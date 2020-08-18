"""
Underscores added to names

Dunder (double under) methods such as __init__ are special Python methods that
Python looks for. Therefore, it is a good practice to not define our own dunder
methods.

Python does not support private attributes or methods. Therefore, if something
is not intended to be used ouside of the class, then an underscore is added.

secret = intended for public use
_secret = intended for private use

Name Mangling:
If you use __ before an attribute, Python will change the name of the attribute.
These attributes are changed into _'Class Name'__'attribute name'
"""

class Person:
    def __init__(self):
        self.name = 'Tony'
        self._secret = 'hi!'
        self.__message = "I like turtles!"

p = Person()

print(p.name)               # Tony
print(p._secret)            # hi!
print(p.__message)          # AttributeError: Person object has no attribute __message
print(p._Person__message)   # I like turtles!