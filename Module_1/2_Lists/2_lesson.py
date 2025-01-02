def swap_my(items):
    if len(items) > 1:
        temp_item = items[0]
        items[0] = items[-1]
        items[-1] = temp_item
    return items

def swap(items):
    if len(items) < 2:
        return items
    items[0], items[-1] = items[-1], items[0]
    return items


print(swap([])) # []
print(swap([1])) # [1]
print(swap([1, 2])) # [2, 1]
print(swap(['one', 'two', 'three'])) # ['three', 'two', 'one']