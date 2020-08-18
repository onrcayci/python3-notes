"""
String Representation Example

The __repr__ method is one of several ways to provide a nicer string
representation.

There is also several other dunders to return classes in string formats
(notably __str__ and __format__), and choosing one is a bit complicated!
"""

class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f'There are currently {cls.active_users} active users.'
    
    @classmethod
    def from_string(cls, data_string):
        first, last, age = data_string.split(',')
        cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
    def __repr__(self):
        return f'{self.first} is {self.age}'
    
    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    def likes(self, thing):
        return f"{self.first} likes {thing}"
    
    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}, {self.first}"

tom = User.from_string('Tom,Jones,89')
print(tom)                              # Tom is 89