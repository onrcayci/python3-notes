"""
Keyword Arguments
"""

def exponent(num, power=2):
    return num ** power

print(exponent(2,3))            # 8
print(exponent(3))              # 9
print(exponent(power=3, num=4)) # 64
print(exponent(num=4, power=3)) # 64

"""
**kwargs

A special operator we can pass to functions.

Gathers remaining keyword arguments as a dictionary.
"""

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}.")

fav_colors(colt='purple')               # colt's favorite color is purple.
fav_colors(colt='purple', ruby='red')   # colt's favorite color is purple. ruby's favorite color is red.