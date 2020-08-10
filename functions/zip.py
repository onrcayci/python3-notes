'''
zip

Make an iterator that aggregates elements from each of the iterables.
Returns an iterator of tupbles, where the i-th tuple contains the i-th element from
each of the argument sequences or iterables.
The iterator stops when the shortest input iterable is exhausted.
'''

first_zip = zip([1,2,3], [4,5,6])
list(first_zip) # [(1, 4), (2, 5), (3, 6)]
dict(first_zip) # {1: 4, 2: 5, 3: 6}