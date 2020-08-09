"""
Dictionary Comprehensions

syntax: { ____:____ for ____ in ____ }
"""

numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key,value in numbers.items()}
print(squared_numbers)  # {'first': 1, 'second': 4, 'third': 9}

# Making a dictionary from a list

{num: num ** 2 for num in [1, 2, 3, 4, 5]}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Conditional logic with dictionary comprehension

num_list = [1, 2, 3, 4]
{ num:('even' if num % 2 == 0 else 'odd') for num in num_list } # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
