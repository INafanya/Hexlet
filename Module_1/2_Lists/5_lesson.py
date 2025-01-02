def add_prefix(names, prefix):
    new_names = []
    for name in names:
        _pref_name = prefix + ' ' + name
        new_names.append(_pref_name)
    return new_names

# BEGIN
def add_prefix(coll, prefix):
    result = []
    for word in coll:
        result.append(f"{prefix} {word}")
    return result
# END