def memoizing(psc):

    def inner(func):
        memory = {}

        def wrapper(num):
            if num in memory:
                return memory[num]
            else:
                result = func(num)
                memory[num] = result
                if len(memory) > psc:
                    memory.pop(next(iter(memory)))
            return result
        return wrapper
    return inner


# @memoizing(3)
# def f(x):
#     print('Calculating...')
#     return x * 10

# print(f(1))
# # => Calculating...
# # 10
# print(f(1))  # будет "вспомнено"
# # 10
# print(f(2))
# # => Calculating...
# # 20
# print(f(3))
# # => Calculating...
# # 30
# print(f(4))  # вытеснит запомненный результат для "1"
# # => Calculating...
# # 40
# print(f(1))  # будет перевычислено
# # => Calculating...
# # 10
# print(f(1))
arguments = []

@memoizing(3)
def inc(argument):
    arguments.append(argument)
    return argument + 1

inc(inc(inc(0)))
print(arguments)
inc(inc(inc(0)))
print(arguments)
inc(10)
print(arguments)
inc(0)
print(arguments)