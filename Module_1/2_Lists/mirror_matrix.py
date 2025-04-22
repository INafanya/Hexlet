def mirror_matrix(coll):
    if not coll:
        return coll
    lenght = len(coll[0])
    if lenght == 1:
        return
    print(coll)
    # print(len(coll[0]))
    l = lenght - lenght // 2

    for row in coll:
        print(row)
        if lenght % 2 == 0:
            j = l - 1
        else:
            j = l - 2
        for i in range(l, lenght):
            row[i] = row[j]
            j -= 1
            print(row[i])
    return coll

empty_row = [
        [],
    ]

text_sample = [
    ['aa', 'bb', 'cc'],
    ['11', '22', '33'],
]

text_sample_2 = [
    ['aa', 'bb', 'cc', 'dd'],
    ['11', '22', '33', '44'],
]
# print(mirror_matrix([[42]]))
# print(mirror_matrix(empty_row))
print(mirror_matrix(text_sample))
# print(mirror_matrix(text_sample_2))

def mirror_matrix(matrix):
    if matrix:
        half_len = len(matrix[0]) // 2
        for line in matrix:
            line[half_len:] = line[-half_len - 1::-1]