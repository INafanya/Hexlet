from hash_table import get_hash


# BEGIN (write your solution here)
def get_or_default(hash_table, key, default):
    hash = get_hash(key)
    data = hash_table[hash]
    result = default if data is None else data[1]
    return result
# END
