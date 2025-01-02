def calculate_sum(items):
    if len(items) == 0:
        return 0
    sum = 0
    for item in items:
        if item % 3 == 0:
            sum += item
    return sum