def get_same_parity(listing):
    if len(listing) == 0:
        return listing
    result = []
    even_check = listing[0] % 2
    for number in listing:
            if number % 2 == even_check:
                result.append(number)
    return result


# BEGIN
def get_same_parity_(coll):
    # проверить на пустоту списки можно и через not
    if not coll:
        return []
    result = []
    remainder = abs(coll[0]) % 2

    for item in coll:
        if abs(item) % 2 == remainder:
            result.append(item)
    return result
# END