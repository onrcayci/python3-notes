"""
unittest module

Python comes with a built-in module called unittest.

You can write unit tests encapsulated as classes that inherit from unittest.TestCase.

This inheritance gives you access to many assertion herlpers that let you test the
behavior of your functions.

You can run tets by calling unittest.main().
"""

import unittest

class Tests(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()