def rotated_left(data):
    return data[1:] + data[:1]

def rotated_right(data):
    return data[-1:] + data[:-1]


print(rotated_left("ABCD"))  # "BCDA"
print(rotated_right([1, 2, 3, 4]))  # "[4, 1, 2, 3]"
