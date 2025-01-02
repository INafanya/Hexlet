def sum_of_square_digits(number):
    return sum(int(x) ** 2 for x in str(number))


def is_happy_number(number):
    if number < 10:
        number = number ** 2
    while number >= 10:
        number = sum_of_square_digits(number)
    return number == 1

print(is_happy_number(13))
