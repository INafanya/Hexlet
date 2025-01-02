def calculate_average(lists):
    if len(lists) == 0:
        return None
    list_lenght = len(lists)
    _summ = 0
    for number in lists:
        _summ += number
    return _summ / list_lenght