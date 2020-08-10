"""
Generator Expressions

If you don't need to access the content of a list afterwards, generator expressions are more
helpful since they take up less space.
"""

import sys

list_comp = sys.getsizeof([x * 10 for x in range(1000)])    # 9024 bytes
gen_exp = sys.getsizeof(x *10 for x in range(1000))         # 88 bytes