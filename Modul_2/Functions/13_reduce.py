from functools import reduce

def group_by(coll, agr_feature):
    users_by_key = {}
    for user in coll:
        key = user[agr_feature]
        if key not in users_by_key:
            users_by_key[key] = []
        users_by_key[key].append(user)
    return users_by_key


def group_by_tech(objects, key):
    def reducer(acc, obj):
        # из каждого объекта берётся значение по ключу
        group_name = obj[key]
        # контейнером группы выступает список
        # метод get возвращает пустой список, если в аккумуляторе ничего нет
        group = acc.get(group_name, [])
        # возвращается новый словарь аккумулятора
        # старый аккумулятор обновляется
        # для текущей группы записывается новый список с данными
        return {**acc, group_name: group + [obj]}

    return reduce(reducer, objects, {})

students = [
    {'name': 'Tirion', 'class': 'B', 'mark': 3},
    {'name': 'Keit', 'class': 'A', 'mark': 3},
    {'name': 'Ramsey', 'class': 'A', 'mark': 4},
]

print(group_by_tech(students, 'mark'))