def get_intersection_of_sorted_lists(coll_1, coll_2):
    idx_1 = 0
    idx_2 = 0
    len_1 = len(coll_1)
    len_2 = len(coll_2)
    result = []
    while idx_1 < len_1 and idx_2 < len_2:
        if coll_1[idx_1] == coll_2[idx_2]:
            result.append(coll_1[idx_1])
            idx_1 += 1
            idx_2 += 1
        elif coll_1[idx_1] > coll_2[idx_2]:
            idx_2 += 1
        else:
            idx_1 += 1
    result = list(set(result))
    result.sort()
    return result


print(get_intersection_of_sorted_lists([10, 11, 24], [10, 13, 14, 18, 24, 30])); # [10, 24]

print(get_intersection_of_sorted_lists([10, 11, 24], [-2, 3, 4])); # []

print(get_intersection_of_sorted_lists([], [2])); # []

print(get_intersection_of_sorted_lists([1, 2, 2, 3, 4], [2, 2, 3, 5])) # [2, 3]

print(get_intersection_of_sorted_lists([3, 5, 10], [10, 12, 19, 21]))
print(get_intersection_of_sorted_lists([10, 11, 24, 30], [10, 13, 14, 18, 24, 30]))