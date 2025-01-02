opening_symbols = ['(', '[', '{', '<']
closing_symbols = [')', ']', '}', '>']


def are_symbols_balanced(expression):
    stack = []
    for char in expression:
        if char in opening_symbols:
            stack.append(char)
        elif char in closing_symbols:
            if not stack or opening_symbols.index(stack[-1]) != closing_symbols.index(char):
                return False
            stack.pop()
    return not stack


# are_symbols_balanced('(>)');  # False
# are_symbols_balanced('()');  # True
# are_symbols_balanced('{}[]');  # True
# are_symbols_balanced('[()]');  # True
print(are_symbols_balanced('({}[])'));  # True
# are_symbols_balanced('{<>}}'); # False
# print(are_symbols_balanced('([)]')); # False