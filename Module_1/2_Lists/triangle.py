def triangle(number):
    pascal = [[1]]
    for i in range(1, number + 1):
        # print(f'i: {i}')
        prev_num = 0
        stack = []
        # print(f'pascal: {pascal}')
        for num in pascal[i-1]:
            stack.append(prev_num + num)
            prev_num = num
            # print(f'stack: {stack}')
        stack.append(1)
        pascal.append(stack)
    for row in pascal:
        print(row)
    print(pascal[number])

# BEGIN
# Определяем функцию для вычисления факториала
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def triangle(row_number):
    numbers_count = row_number + 1
    line = []
    calculated = fact(row_number)
    for i in range(numbers_count):
        # Для вычисления числа заданной строки используем формулу
        # расчёта биноминальных коэффициентов С(n, k) = n! / (k! * (n - k)!)
        line.append(calculated / (fact(i) * fact(row_number - i)))
    return line

triangle(0)