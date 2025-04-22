def validate_passwords(pass_coll):
    no_short = all(len(pas) > 7 for pas in pass_coll)
    digits = any(any(char.isdigit() for char in pas) for pas in pass_coll)
    uppercase = any(any(char.isupper() for char in pas) for pas in pass_coll)
    space = all(' ' not in pas for pas in pass_coll)
    return no_short & digits & uppercase & space
    
passwords = {
        'short': ['short', '1234567'],
        'no_digits': ['password', 'strongPass'],
        'no_uppercase': ['password123', 'strongpass1'],
        'contains_space': ['password 123', 'strongPass1'],
        'valid': ['password123', 'Password123', 'StrongPass1']
    }

        
        
if __name__ == '__main__':
    for typ, pas in passwords.items():
        print(f"{typ=}, {pas=}, {validate_passwords(pas)}")