def transposed(matrix):
    print(matrix)
    len_row = len(matrix[0])
    len_str = len(matrix)
    transposed_matrix = [[0 for i in range(len_str)] for j in range(len_row)]
    print(f"str: {len_str}")
    print(f"row: {len_row}")

    if len_str == 1:
        for i in range(len_row):
            transposed_matrix[i][0] = matrix[0][i]
    # if len_row == 1:
    #     for i in range(len_row):
    #         transposed_matrix[0][i] = matrix[i][0]
    else:# len_str < len_row:
        for i in range(len_row):
            for j in range(len_str):
                transposed_matrix[i][j] = matrix[j][i]
    # elif len_str > len_row:
    #     for i in range(len_str):
    #         for j in range(len_row):
    #             transposed_matrix[i][j] = matrix[j][i]
    print(transposed_matrix)
    return transposed_matrix


# print(transposed([[1]]))  # [[1]]
# print(transposed([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
# print(transposed([[1, 2], [3, 4], [5, 6]]))  # [[1, 3, 5], [2, 4, 6]]
# print(transposed([[4, 5, 6]]))
print(transposed([[1], [2], [3],]))


SAMPLES = (
    # single cell
    ([[42]], [[42]]),

    # column
    ([
        [1],
        [2],
        [3],
    ], [
        [1, 2, 3],
    ]),

    # row
    ([
        [4, 5, 6],
    ], [
        [4],
        [5],
        [6],
    ]),

    # square matrix
    ([
        [10, 20],
        [30, 40],
    ], [
        [10, 30],
        [20, 40],
    ]),

    # rectangle matrix
    ([
        ['d', 'o'],
        ['r', 'e'],
        ['m', 'i'],
    ], [
        ['d', 'r', 'm'],
        ['o', 'e', 'i'],
    ]),
)


def test_transposed_reversibility():
    for matrix, _ in SAMPLES:
        print(transposed(transposed(matrix)) == matrix)


#test_transposed_reversibility()

def transposed(matrix):
    result = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        result.append(new_row)
    return result


""" Альтернативное решение с использованием zip и оператора распаковки
def transposed(matrix):
    result = []
    for column in zip(*matrix):
        result.append(list(column))
    return result
"""