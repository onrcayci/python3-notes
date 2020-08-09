"""
Parameter Ordering

1. parameters
2. *args
3. default parameters
4. **kwargs
"""

def display_info(a, b, *args, instructor="Onur", **kwargs):
    return [a, b, args, instructor, kwargs]

print(display_info(1, 2, 3, last_name='Cayci', job='Developer'))
# a = 1
# b = 2
# args = (3,)
# instructor = "Onur"
# kwargs = {'last_name': 'Cayci', 'job': 'Developer'}