def is_continuous_sequence(coll):
    if len(coll) < 2:
        return False
    for x, y in zip(coll, coll[1:]):
        if (y - x) != 1:
            return False
    return True




print(is_continuous_sequence([7]))
print(is_continuous_sequence([5, 3, 2, 8]))
print(is_continuous_sequence([10, 11, 12, 14, 15]))
print(is_continuous_sequence([10, 11, 11, 12]))
print(is_continuous_sequence([5, 6, 6, 8]))
print(is_continuous_sequence([0, 1, 2, 3]))
print(is_continuous_sequence([-5, -4, -3]))
print(is_continuous_sequence([10, 11, 12, 13]))