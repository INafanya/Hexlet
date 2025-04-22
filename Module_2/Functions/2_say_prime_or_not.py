def say_prime_or_not(number):
    result = is_prime_number(number)
    print_result(result)


def is_prime_number(number):
    if number < 2:
        return 'no'
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return 'no'
        divider += 1
    return 'yes'


def print_result(text):
    print(text)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def say_prime_or_not(num):
    answer = 'yes' if is_prime(num) else 'no'
    print(answer)