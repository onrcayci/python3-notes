"""
Doctests

You have the option to write tests into your docstring in python.
"""

def add(a, b):
    """
    >>> add(2, 3)
    5
    >>> add(100, 200)
    300
    """
    return a + b

# command line command to run the doctests:
# python -m doctest -v filename.py