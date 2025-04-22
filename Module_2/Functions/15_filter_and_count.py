from collections import Counter



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

def get_free_domains_count(coll):
    FREE_EMAIL_DOMAINS = [
    'gmail.com',
    'yandex.ru',
    'hotmail.com',
    'yahoo.com',
]


    # filtered_coll = list(filter(lambda email: email.split('@')[1] in FREE_EMAIL_DOMAINS, coll))
    # domains = [email.split('@')[1] for email in coll if email.split('@')[1] in FREE_EMAIL_DOMAINS]
    return dict(Counter([email.split('@')[1] for email in coll if email.split('@')[1] in FREE_EMAIL_DOMAINS]))

if __name__ == '__main__':
    print(get_free_domains_count(emails))

