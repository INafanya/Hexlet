def get_first_name(string):
    return string.split('_')[0]



def sort_by(key, users):
    return sorted(users, key=key)


users = ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]

print(sort_by(get_first_name, users))  # ["Boba_Fett", "Luke_Skywalker", "Vader_Darth"]
print(users)

