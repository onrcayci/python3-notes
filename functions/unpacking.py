"""
Argument Unpacking: Using * as an Argument

We can use * as an argument to a function to "unpack" values.
"""

def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)

sum_all_values(1, 30, 2, 5, 6)  # 44

# passing the values of a list

nums= [1, 2, 3, 4, 5, 6]
sum_all_values(nums)    # error
sum_all_values(*nums)   # 21

"""
Dictionary Unpacking: Using ** as an Argument

We can use ** as an argument to a function to "unpack" dictionaries.
"""

def display_names(first, second):
    print(f'{first} says hello to {second}')

names = {'first': 'Onur', 'second': 'Rusty'}
display_names(first='Onur', second='Rusty') # Onur says hello to Rusty
display_names(names)                        # error: missing one required argument
display_names(**names)                      # Onur says hello to Rusty