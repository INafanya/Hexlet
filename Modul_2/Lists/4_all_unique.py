def all_unique(col):
    return len(col) == len(set(col))

print(all_unique('helo'))



    # all_unique([])
    # # True
    # all_unique([1, 2, 3])
    # # True
    # all_unique([1, 2, 1])
    # # False