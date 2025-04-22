def enlarge(image):
    # print(image)
    result = []
    for row in image:
        stack = []
        # print(f'row: {row}')
        for item in row:
            stack.append(str(item) * 2)
        row = ''.join(stack)
            # print(stack)
            # print(new_row)
        # result.append(row)
        # result.append(row)
        result.extend([row] * 2)
    print(result)

frame = [
    '****',
    '*  *',
    '*  *',
    '****'
]

enlarge(frame)