def make_user(name, age):
    user_dict = {
        'name': name,
        'age': age
    }
    return user_dict


def format_user(users_dict):
    user = users_dict[list(users_dict.keys())[0]]
    age = users_dict[list(users_dict.keys())[1]]
    return f"{user}, {age}"


if __name__ == '__main__':
    print(format_user(make_user('Bob', 42)))