def multiply(matrix_a, matrix_b):
    # cols = len(matrix_b[0])
    # rows = len(matrix_a)
    # if cols != rows:
    #     print('Матрицы не согласованы')
    # mult_matrix = [[0 for _ in range(cols)] for _ in range(len(matrix_a))]
    #
    # for row_a, row_res in zip(matrix_a, mult_matrix):
    #     for x in range(cols):
    #         for y, row_b in enumerate(matrix_b):
    #             row_res[x] += row_a[y] * row_b[x]

    # result = [[sum(a * b for a, b in zip(matrix1_row, matrix2_col)) for matrix2_col in zip(*matrix_b)] for matrix1_row in matrix_a]

    mult_matrix = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            m = 0
            for k in range(len(matrix_a[0])):
                m += matrix_a[i][k] * matrix_b[k][j]
            row.append(m)
        mult_matrix.append(row)

        for row in mult_matrix:
            print(row)
    return mult_matrix



A = [[1, 2, 1],
     [0, 1, 0],
     [2, 3 ,4],
     ]
B = [[2, 5],
     [6, 7],
     [1, 8],
     ]

C = [[2, 5], [6, 7], [1, 8]]
D = [[1, 2, 1], [0, 1, 0]]




multiply(A, B)
# multiply(C, D)

