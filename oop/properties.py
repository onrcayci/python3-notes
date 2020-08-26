"""
Object Properties

There is another way to define private properties for objects, which is using the
property decorator (@property). This will act as a normal property when called on
the object, however it will be used as a getter and setter of the private property.
"""

class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be negative!")
    
onur = Person('Onur', 'Cayci', -1)
print(onur.age)                         # 0
onur.age = 22
print(onur.age)                         # 22
