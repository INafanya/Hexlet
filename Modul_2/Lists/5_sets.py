def toggle(col_set, flag):
    if flag in col_set:
        col_set.remove(flag)
    else:
        col_set.add(flag)
    print(col_set)


toggle('read_only', )

