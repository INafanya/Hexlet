def get_weekends(day_format='long'):
    if day_format == 'long':
        result = ['saturday', 'sunday']
    elif day_format == 'short':
        result = ['sat', 'sun']
    else:
        result = 'Wrong parameter'
    return result

get_weekends('long') # ['saturday', 'sunday']
get_weekends('short') # ['sat', 'sun']