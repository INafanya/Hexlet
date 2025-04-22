def memoized(func):
    memory = {}

    def wrapper(num):
        if num in memory:
            return memory[num]
        else:
            print('Calculating...')
            result = func(num)
            memory[num] = result
        return result
    return wrapper



@memoized
def f(x):
    print(x * 10)
    return x * 10

f(5)
f(5)
