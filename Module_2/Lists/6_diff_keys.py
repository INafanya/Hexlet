def diff_keys(dict_old, dict_new):
    kept = dict_old & dict_new
    added = dict_new - dict_old
    removed = dict_old - dict_new
    diff_result = {'kept': kept, 'added': added, 'removed': removed}
    return diff_result
