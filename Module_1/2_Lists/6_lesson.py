def reverse(items):
    lenght = len(items)
    for index in range(0, lenght // 2):
        items[index], items[lenght - index - 1] = items[lenght - index - 1], items[index]

    return items