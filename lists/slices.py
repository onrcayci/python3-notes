"""
List Slicing

syntax: some_list[start:end:step]
"""

first_list = [1, 2, 3, 4]
second_list = [1, 2, 3, 4, 5, 6]

# First Parameter for Slice: start

first_list[1:]  # [2, 3, 4]
first_list[3:]  # [4]
first_list[-1:] # [4]
first_list[-3:] # [2, 3, 4]
first_list[0:]  # copy of the list first_list, first_list == first_list[0:] True, first_list is first_list[0:] False

# Second Parameter for Slice: end

first_list[:2]  # [1, 2]
first_list[:4]  # [1, 2, 3, 4]
first_list[1:3] # [2, 3], (indeces from 1 to 3)
first_list[:-1] # [1, 2, 3]
first_list[1:-1]# [2, 3]

# Third Parameter for Slice: step

second_list[1::2]   # [2, 4, 6]
second_list[::2]    # [1, 3, 5]

# with negative steps, reverses the order

second_list[1::-1]  # [2, 1]
second_list[:1:-1]  # [6, 5, 4, 3]
second_list[2::-1]  # [3, 2, 1]

# Reversing lists/strings with slice

string = "This is fun!"
string[::-1]    # "!nuf si sihT"

# Modifying portions of lists

numbers = [1, 2, 3, 4, 5]
number[1:3] = ['a', 'b', 'c']
numbers # [1, 'a', 'b', 'c', 4, 5]