import operator
def rpn_calc(coll):
    new_coll = coll.copy()
    result = 0
    iteration = len(coll) // 2
    while iteration > 1:
        for i in range(len(new_coll)):
            if str(new_coll[i]) == '+':
                a = new_coll[i-2]
                b = new_coll[i-1]
                result += a + b
                new_coll = new_coll[:i-2] + [result] + new_coll[i+1:]
                iteration -= 1
                break
            elif str(new_coll[i]) == '-':
                a = new_coll[i - 2]
                b = new_coll[i - 1]
                result += a - b
                new_coll = new_coll[:i-2] + [result] + new_coll[i+1:]
                iteration -= 1
                break
            elif str(new_coll[i]) == '/':
                a = new_coll[i - 2]
                b = new_coll[i - 1]
                result += a / b
                new_coll = new_coll[:i-2] + [result] + new_coll[i+1:]
                iteration -= 1
                break
            elif str(new_coll[i]) == '*':
                a = new_coll[i - 2]
                b = new_coll[i - 1]
                result += a * b
                new_coll = new_coll[:i-2] + [result] + new_coll[i+1:]
                iteration -= 1
                break
    return result


# print(rpn_calc([1, 2, '+', 4, '*', 3, '+']))  # 15
print(rpn_calc([7, 2, 3, '*', '-']))  # 1