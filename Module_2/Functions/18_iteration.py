def factorial(n):
    if n == 0:
        return 1

    def inner(counter, acc):
        if counter == 1:
            return acc
        return inner(counter - 1, counter * acc)

    return inner(n, 1)



def smallest_divisor(num: int) -> int:
    if num == 1:
        return 1

    def inner(divisor):
        if divisor > num // 2:
            return num
        if not num % divisor:
            return divisor
        return inner(divisor + 1)
    return inner(2)


print(smallest_divisor(1789600698066371))