def normalize_url(url):
    norm = 'https://'
    if url[:8] == norm:
        return url
    elif url[:7] == 'http://':
        return norm + url[7:]
    else:
        return norm + url

print(normalize_url('https://ya.ru'))  # https://ya.ru
print(normalize_url('google.com'))  # https://google.com
print(normalize_url('http://ai.fi'))  # https://ai.fi