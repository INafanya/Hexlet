# Функция вычисления числа Фибоначчи по его порядковому номеру (n)
# F(n) = F(n-1) + F(n-2)
def fib(index):
    n_2 = 0                     # F(n-2)
    n_1 = 1                     # F(n-1)
    fibonachchi = 1             # Число Фибоначчи
    for i in range(1, index):
        fibonachchi = n_1 + n_2
        n_2 = n_1
        n_1 = fibonachchi
    print(f'Число Фибоначчи: {fibonachchi}')

fib(7)