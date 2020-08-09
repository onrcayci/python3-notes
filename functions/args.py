"""
*args

A special operator we can pass to functions.

Gathers remaining arguments as a tuple.
"""

def sum_all_nums(num1, num2, num3):
    return num1 + num2 + num3

print(sum_all_nums(4, 6, 9))    # 19
print(sum_all_nums(4, 6))       # Error: no value for argument num3

def sum_with_args(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_with_args(4, 6, 9))   # 19
print(sum_with_args(4, 6))      # 10