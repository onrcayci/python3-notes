"""
Filter

There is a lambda for each value in the iterable.
Returns filter object which can be converted into other iterables.
The object contains only the values that return true to the lambda.
"""

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

inactive_users = filter(lambda u: not u['tweets'], users)
list(inactive_users)        # [{"username": "jeff", "tweets": []}, {"username": "bob123", "tweets": []}, {"username": "guitar_gal", "tweets": []}]

inactive_usernames = map(lambda user: user['username'], filter(lambda user: not user['tweets'], users))
list(inactive_usernames)    # ['jeff', 'bob123', 'guitar_gal']