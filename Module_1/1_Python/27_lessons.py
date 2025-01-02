#age1 = 2001
#age2 = 2018
def get_age_difference(age1, age2):
    return 'The age difference is ' + str(abs(age1 - age2))

actual = get_age_difference(2001, 2018)
print(actual)