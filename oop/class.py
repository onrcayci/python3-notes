"""
__init__ method for Classes

Classes in Python can have a special __init__ method, which gets called every
time you create an instance of the class (instantiate).

Instantiating a Class:
Creating an object that is an instance of a class is called instanciating a class.

self keyword:
It refers to the current class instance. (Similar to 'this' in Java or JavaScript)
"""

class User1:
    
    def __init__(self):
        print('A NEW USER HAS BEEN MADE!')

user1 = User1()  # prints 'A NEW USER HAS BEEN MADE!'

class User2:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

user2 = User2('Joe', 'Smith', 68)
# user2.first == 'Joe'
# user2.last == 'Smith'
# user2.age == 68