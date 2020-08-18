"""
Class Attributes

General attribute that is referenced by the static class. All of the instances
refer to the same attribute in the memory. So if you call id() method on the
class attribute, it will be the same for all the instances and the static class.
"""

class User:

    active_users = 0

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

print(User.active_users)            # 0
user1 = User('Joe', 'Smith', 68)
user2 = User('Blanca', 'Lopez', 41)
print(User.active_users)            # 2
print(user2.logout())               # Blanca has logged out
print(User.active_users)            # 1