def get_total_amount(wallet, currency):
    summ = 0
    for item in wallet:
        item = item.split()
        if item[0] == currency:
            summ += int(item[1])
    return summ

# BEGIN
def get_total_amount(wallet, currency):
    sum = 0
    for bill in wallet:
        curret_currency, amount = bill.split(' ')
        if curret_currency != currency:
            continue
        sum += int(amount)
    return sum
# END


money1 = [  'eur 10', 'usd 1', 'usd 10', 'rub 50', 'usd 5',]
print(get_total_amount(money1, 'usd')) # 16

money2 = ['eur 10', 'usd 1', 'eur 5', 'rub 100', 'eur 20', 'eur 100', 'rub 200',]
print(get_total_amount(money2, 'eur')) # 135

money3 = ['eur 10', 'rub 50', 'eur 5', 'rub 10', 'rub 10', 'eur 100', 'rub 200',]
print(get_total_amount(money3, 'rub')) # 270