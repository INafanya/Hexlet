from itertools import chain


def length(col):
    if not col:
        return 0
    head, *new_col = col
    if not new_col:
        return 1
    return 1 + length(new_col)
    
def length_teach(list):
    if not list:
        return 0
    _, *tail = list
    return 1 + length(tail)


def reverse_range_teach(begin, end):
    if begin == end:
        return [begin]
    return [end] + reverse_range(begin, end - 1)


def reverse_range0(begin, end):
    *new_col, tail = range(begin, end + 1)
    if not new_col:
        return tail
    return sum([tail, reverse_range(begin, end - 1)], [])


def reverse_range(begin, end):
    result = []
    while begin <= end:
        result.append(end)
        end -= 1
    return result


def reverse_range2(begin, end, arr=[]):
    if(begin > end):
        return arr;
 
    arr.append(end);
    end -= 1;
    return reverse_range(begin, end, arr);


def filter_positive(list):
    if not list:
        return []
    head, *tail = list
    if head > 0:
        return [head] + filter_positive(tail)
    return filter_positive(tail)


def filter_positive(col):
    result = []
    for num in col:
        if num > 0:
            result.append(num)
    return result

print(length([]))

print(reverse_range(1,5))
print(filter_positive([1, -2, 3]))