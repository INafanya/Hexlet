def unique(collection):
    seen = set()
    unique_items = []
    for item in collection:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items


def get_same_count(lst_1, lst_2):
    uniq_list_1 = unique(lst_1)
    uniq_list_2 = unique(lst_2)
    uniq_sum = 0
    for num in uniq_list_1:
        if num in uniq_list_2:
            uniq_sum += 1
    return uniq_sum

print(get_same_count([1, 3, 2, 2], [3, 1, 1, 2, 5])) # 3
