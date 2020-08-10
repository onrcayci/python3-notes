"""
sorted

Return a new sorted list from the items in iterable.
"""

nums = [6, 1, 8, 2]
sorted(nums)    # [1, 2, 6, 8]
print(nums)     # [6, 1, 8, 2]

# for dictionaries, you have to pass in how they will be sorted.

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

sorted(users, key=len)                              # the list will be sorted depending on the length of the dictionaries
sorted(users, key=lambda user: user['username'])    # the list is sorted in an alphabetical order of their username
sorted(users, key=lambda user: len(user['tweets'])) # the list is sorted from the shortest tweets to the longest