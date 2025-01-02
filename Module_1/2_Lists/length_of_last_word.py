def lengthh_of_last_word(text):
    text2 = text.replace('\t', ' ').replace('\n', ' ').strip().split(' ')
    return len(text2[-1:][0])

def length_of_last_word(string):
    words = string.split()
    print(words)
    if not words:
        return 0
    last_word = words[-1]
    return len(last_word)


print(length_of_last_word('')) # 0
print(length_of_last_word(' \t\n')) # 0
print(length_of_last_word('hi')) # 2
print(length_of_last_word('Hexlet, hi')) # 2
print(length_of_last_word('  cat')) # 3
print(length_of_last_word('man in black')) # 5
print(length_of_last_word('hello, world!')) # 6
print(length_of_last_word('hello, wOrLd!    ')) # 6
print(length_of_last_word('hello\t\nworld')) # 5