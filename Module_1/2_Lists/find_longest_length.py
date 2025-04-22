def find_longest_length(text):
    max_length = 0
    for i, _ in enumerate(text):
        print(i)
        unique_chars = []
        for char in text[i:]:
            print(char)
            print(unique_chars)
            if char in unique_chars:
                break
            unique_chars.append(char)
        print(f'max: {max_length}')
        print(f'len: {len(unique_chars)}')
        max_length = max(max_length, len(unique_chars))
    print(max_length)
    return max_length



test1 = 'abcddef'  # 5

find_longest_length(test1)
