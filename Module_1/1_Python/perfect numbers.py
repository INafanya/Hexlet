def is_perfect(number):
    count = 0
    if number > 0:
        for i in range(1, number):
            if number % i == 0:
                count += i
    else:
        return False
    return count == number

print(is_perfect(6))