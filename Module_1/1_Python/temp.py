def find_expensive_items(prices_string):
    result = ''
    print(result)
    coll = list(map(int, prices_string.split(',')))
    print(coll)
    summ = sum(coll)
    count = len(coll)
    avg = summ / count

    for num in coll:
        if num > avg:
            result += '\n ' + str(num)

    if not result:
        return 'Нет'

    return result




print(find_expensive_items('10,20,30,40,50'))