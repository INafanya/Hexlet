def format_person_info(name, age, **kwargs):
    result = f'Name: {name}, Age: {age}'
    sorted_kwargs = dict(sorted(kwargs.items()))
    for key, value in sorted_kwargs.items():
        result += f', {key.capitalize()}: {value}'
    return result
    
    


basic_info = ('Alice', 30)
additional_info = {'city': 'New York', 'job': 'Engineer', 'hobby': 'painting'}
print(format_person_info(*basic_info, **additional_info))


def format_person_info_teacher(name, age, **kwargs):
    base_info = f"Name: {name}, Age: {age}"

    if kwargs:
        additional_info = []
        for key, value in sorted(kwargs.items()):
            additional_info.append(f"{key.capitalize()}: {value}")
        return f"{base_info}, {", ".join(additional_info)}"
    else:
        return base_info