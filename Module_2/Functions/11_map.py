from itertools import chain

def get_children(coll):
    children = map(lambda user: user['children'], coll)
    return list(chain.from_iterable(list(children)))


users = [
    {
        'name': 'Tirion',
        'children': [
            {'name': 'Mira', 'birthday': '1983-03-23'},
        ],
    },
    {'name': 'Bronn', 'children': []},
    {
        'name': 'Sam',
        'children': [
            {'name': 'Aria', 'birthday': '2012-11-03'},
            {'name': 'Keit', 'birthday': '1933-05-14'},
        ],
    },
    {
        'name': 'Rob',
        'children': [
            {'name': 'Tisha', 'birthday': '2012-11-03'},
        ],
    },
]

print(get_children(users))