def count_uniq_chars(text):
    return len(set(text))


text = 'You know nothing Jon Snow'
print(count_uniq_chars(text))


def count_uniq_chars(text):
    uniq_chars = []

    for char in text:
        if char not in uniq_chars:
            uniq_chars.append(char)

    return len(uniq_chars)