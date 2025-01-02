def encrypt(text):
    result = ''
    text_len = len(text)
    for index in range(0, text_len, 2):
        print(index)
        if index + 2 <= text_len:
            result += text[index + 1] + text[index]
        else:
            result += text[index]
    return result


def encrypt_(text):
    text_len = len(text)
    result = ''
    i = 0
    while i < text_len:
        if i + 2 <= text_len:
            result += text[i + 1] + text[i]
        else:
            result += text[i]
        i += 2
    return result


def encrypt_teacher(word):
    result = ''
    i = 0
    while i < len(word):
        result += word[i:i + 2][::-1]
        i += 2
    return result

print(encrypt("move")) # 'omev'
print(encrypt("attack")) # 'taatkc'
print(encrypt_("go!")) # 'og!'

