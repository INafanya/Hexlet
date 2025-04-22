emails = [
    'info@gmail.com',
    'info@yandex.ru',
    'info@hotmail.com',
    'mk@host.com',
    'support@hexlet.io',
    'key@yandex.ru',
    'sergey@gmail.com',
    'vovan@gmail.com',
    'vovan@hotmail.com',
]

def test(coll):
    FREE_EMAIL_DOMAINS = [
    'gmail.com',
    'yandex.ru',
    'hotmail.com',
    'yahoo.com',
]
    
    for email in coll:
        domain = email.split('@')
        for i in domain:
            if i in FREE_EMAIL_DOMAINS:
                print(i)
        


test(emails)