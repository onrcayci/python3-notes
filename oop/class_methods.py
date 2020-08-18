"""
Class Methods

Class methods are methods (with the @classmethods decorator) taht are not concerned
with instances, but the class itself.

cls is the class, in this case User.
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

user1 = User('Joe', 'Smith', 68)
user2 = User('Blanca', 'Lopez', 41)
print(User.display_active_users())  # There are currently 2 active users
tom = User.from_string('Tom,Jones,89')
print(tom.first)                    # Tom
print(tom.last)                     # Jones