def id_generator(pref):
    user_id = 0

    def make_id():
        nonlocal user_id
        user_id += 1
        return pref + '-' + str(f'{user_id:03}')

    return make_id


result = id_generator("TEST")
print(result)
print(result)
print(result)
