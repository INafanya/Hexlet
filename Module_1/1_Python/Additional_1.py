#Реализуйте функцию is_happy_ticket(), проверяющую является ли номер счастливым (номер — всегда строка). Функция должна возвращать True, если билет счастливый, или False, если нет.
#Подразумевается, что данные на входе всегда корректны, поэтому дополнительные проверки не требуются.
#"Счастливым" называют билет с номером, в котором сумма первой половины цифр равна сумме второй половины цифр. Номера могут быть произвольной длины. Единственное условие — количество цифр всегда четно, например: 33 или 2341.

import os
def is_happy_ticket():
    while True:
        print('''
Введите номер билета или любой символ для выхода
        ''')
        ticket_number = str(input())
        try:
            os.system('cls')
            float(ticket_number)
            pair_lenght = int(len(ticket_number) / 2)
            num_one = ticket_number[:pair_lenght]
            num_two = ticket_number[pair_lenght:]
            sum_one = 0
            sum_two = 0
            if len(ticket_number) % 2 == 0:  # len(num_one) == len(num_two):
                for num in num_one:
                    sum_one += int(num)
                for num in num_two:
                    sum_two += int(num)
                print(f'''
        Первая часть билета: {num_one}
        Вторая часть билета: {num_two}
        {'Поздравляю! Этот билет счастливый' if sum_one == sum_two else 'К сожалению, это обычный билет'}
                        ''')
                # return sum_one == sum_two
            else:
                print(f'Введён некорректный номер билета')
        except ValueError:
            return


is_happy_ticket()