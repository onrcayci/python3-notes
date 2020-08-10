"""
Map
"""

nums = [2, 4, 6, 8, 10]
doubles = map(lambda x: x * 2, nums)
list(doubles)   # [4, 8, 12, 16, 20]

names = [
    {'first': 'Rusty', 'last': 'Steele'},
    {'first': 'Colt', 'last': 'Steele'},
    {'first': 'Blue', 'last': 'Steele'}
]
first_names = list(map(lambda x: x['first'], names))    # ['Rusty', 'Colt', 'Blue']