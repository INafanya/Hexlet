def bubble_sort(coll):
    step = len(coll) - 1
    need_sort_flag = True
    while need_sort_flag:
        need_sort_flag = False
        for i in range(step):
            if coll[i] > coll[i + 1]:
                coll[i], coll[i + 1] = coll[i + 1], coll[i]
                need_sort_flag = True
    return coll

print(bubble_sort([3, 2, 10, -2, 0]))