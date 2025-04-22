import operator
def rpn_calc(coll):
    new_coll = coll.copy()
    for iter in range(len(coll) // 2):
        for i in range(len(new_coll)):
            if str(new_coll[i]) == '+':
                a = new_coll[i-2]
                b = new_coll[i-1]
                result = a + b
                new_coll = new_coll[:i-2] + [result] + new_coll[i+1:]
                break
            elif str(new_coll[i]) == '-':
                a = new_coll[i - 2]
                b = new_coll[i - 1]
                result = a - b
                new_coll = new_coll[:i-2] + [result] + new_coll[i+1:]
                break
            elif str(new_coll[i]) == '/':
                a = new_coll[i - 2]
                b = new_coll[i - 1]
                result = a / b
                new_coll = new_coll[:i-2] + [result] + new_coll[i+1:]
                break
            elif str(new_coll[i]) == '*':
                a = new_coll[i - 2]
                b = new_coll[i - 1]
                result = a * b
                new_coll = new_coll[:i-2] + [result] + new_coll[i+1:]
                break
    return result

# BEGIN
get_operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}.get


def rpn_calc(rpn):
    stack = []
    for elem in rpn:
        op = get_operator(elem)
        if op is not None:
            x = stack.pop()
            y = stack.pop()
            elem = op(y, x)
        stack.append(elem)
    return stack[0]
# END

print(rpn_calc([1, 2, '+', 4, '*', 3, '+']))  # 15
print(rpn_calc([7, 2, 3, '*', '-']))  # 1