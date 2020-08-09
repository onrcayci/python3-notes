"""
List Comprehensions

syntax: [ ____ for ____ in ____ ]
"""

nums = [1, 2, 3]
[x*10 for x in nums]    # [10, 20, 30]
[x/2 for x in nums]     # [0.5, 1.0, 1.5]

# List Comprehension with Conditional Logic

numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]        # [2, 4, 6]
odds = [num for num in numbers if num % 2 != 0]         # [1, 3, 5]
[num*2 if num % 2 == 0 else num/2 for num in numbers]   # [0.5, 4, 1.5, 8. 2.5, 12]

# Nested List Comprehension

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(val) for val in list] for list in lists]        # 1, 2, 3, 4, 5, 6, 7, 8, 9