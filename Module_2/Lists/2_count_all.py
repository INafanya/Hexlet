def count_all(col):
    result = {}
    for item in col:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
    return result


def count_all_teacher(items):
    counters = {}
    for item in items:
        counters[item] = counters.get(item, 0) + 1
    return counters

v1 = count_all(["cat", "dog", "cat"])  # {"cat": 2, "dog": 1}
v2 = count_all("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
v3 = count_all("*" * 20)  # {'*': 20}
print(v1)
print(v2)
print(v3)