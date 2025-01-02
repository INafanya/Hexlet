from itertools import islice
def chunked(size, sequence):
    print(sequence)
    result = []
    if str(sequence) == '':
        return result
    i = 0
    while i < len(sequence):
        if isinstance(sequence, list):
            result.append(list(islice(sequence, i, i + size)))
        elif isinstance(sequence, tuple):
            result.append(tuple(islice(sequence, i, i + size)))
        elif isinstance(sequence, str):
            result.append(sequence[i:i + size])
        i = i + size
    return result

def chunked(size, source):
    result = []
    index = 0
    while index < len(source):
        result.append(source[index:index + size])
        index += size
    return result

print(chunked(2, 'abcd'))  # ['ab', 'cd']
print(chunked(3, 'efhi'))  # ['efh', 'i']
print(chunked(4, 'gklm'))  # ['gklm']
print(chunked(4, ''))  # []
print(chunked(2, 'x'))  # ['x']
print(chunked(2, 'abcdef'))  # ['ab', 'cd', 'ef']

# print(chunked(2, ['a', 'b', 'c', 'd']))  # [['a', 'b'], ['c', 'd']]
# print(chunked(3, ['e', 'f', 'h', 'i']))  # [['e', 'f', 'h'], ['i']]
# print(chunked(4, ['g', 'k', 'l', 'm']))  # [['g', 'k', 'l', 'm']]
# print(chunked(4, []))  # []
# print(chunked(2, ['n']))  # [['n']]
# print(chunked(2, ['a', 'b', 'c', 'd', 'e', 'f']))  # [['a', 'b'], ['c', 'd'], ['e', 'f']]
#
# print(chunked(2, ('A', 'B', 'C', 'D')))  # [('A', 'B'), ('C', 'D')]
# print(chunked(3, ('E', 'F', 'H', 'I')))  # [('E', 'F', 'H'), ('I',)]
# print(chunked(4, ('G', 'K', 'L', 'M')))  # [('G', 'K', 'L', 'M')]
# print(chunked(4, []))  # []
# print(chunked(2, ('N',)))  # [('N',)]
# print(chunked(2, ('A', 'B', 'C', 'D', 'E', 'F')))  # [('A', 'B'), ('C', 'D'), ('E', 'F')]

