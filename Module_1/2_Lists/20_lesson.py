def get_max(coll):
    if not coll:
        return None
    first, *rest = coll
    for num in rest:
        if num > first:
            first = num
    return first

print(get_max([1, 2, 3, 4]))