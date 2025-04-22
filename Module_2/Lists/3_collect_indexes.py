def collect_indexes(col):
    result = {}
    for index in range(len(col)):
        result.setdefault(col[index], []).append(index)
    return result


from collections import defaultdict


def collect_indexes_teacher(items):
    result = defaultdict(list)
    for index, item in enumerate(items):
        result[item].append(index)
    return result

print(collect_indexes("hello"))



    # d = collect_indexes("hello")
    # d["h"]  # [0]
    # d["e"]  # [1]
    # d["l"]  # [2, 3]