def apply_diff(target, diff):
    for key in diff:
        print(f"{key}")
        if key == 'add':
            target.update(diff[key])
        elif key == 'remove':
            target.difference_update(diff[key])
    print(target)

target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}

apply_diff(target, diff)


def apply_diff_teacher(set_for_update, diff):
    set_for_update.update(diff.get('add', {}))
    set_for_update.difference_update(diff.get('remove', {}))