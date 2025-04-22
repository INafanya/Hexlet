from itertools import chain


# BEGIN (write your solution here)
def get_girl_friends(users):
    friends = map(lambda user: user['friends'], users)
    friends_list = chain.from_iterable(list(friends))
    return list(filter(lambda girlfriend: girlfriend['gender'] == 'female', friends_list))
# END

users = [
    {
        'name': 'Tirion',
        'friends': [
            {'name': 'Mira', 'gender': 'female'},
            {'name': 'Ramsey', 'gender': 'male'},
        ],
    },
    {'name': 'Bronn', 'friends': []},
    {
        'name': 'Sam',
        'friends': [
            {'name': 'Aria', 'gender': 'female'},
            {'name': 'Keit', 'gender': 'female'},
        ],
    },
    {
        'name': 'Rob',
        'friends': [
            {'name': 'Taywin', 'gender': 'male'},
        ],
    },
]

print(get_girl_friends(users))