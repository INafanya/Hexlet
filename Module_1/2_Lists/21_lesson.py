def flatten(coll):
    result = []
    for item in coll:
        if isinstance(item, list):
            result = [*result, *item]
        else:
            result = [*result, item]
    return result

print(flatten([1, [3, 2], 9]))


