def get_average(*args):
    return None if len(args) == 0 else sum(args) / len(args)

print(get_average(-3, 4, 2, 10))