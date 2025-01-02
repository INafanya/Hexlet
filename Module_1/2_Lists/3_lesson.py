
def get(items, idx, default=None):
    if (idx < 0 and abs(idx) > len(items)) or idx >= len(items):
        return default
    else:
        return items[idx]



cities = ['moscow', 'london', 'berlin', 'porto', '', True]

print(get(cities, 1)) # 'london'
print(get(cities, -7, 'default'))
print(get(cities, 7, False))
get(cities, 4) # ''
get(cities, 10, 'paris') # 'paris'
get(cities, 5, 'oops') # True
get(cities, -1, 'oops') # True
get(cities, 7) # None