def build_definition_list(definitions_list):
    if not definitions_list:
        return ''
    definitions = []
    for item in definitions_list:
        definitions.append(f'<dt>{item[0]}</dt><dd>{item[1]}</dd>')
    _value = ''.join(definitions)
    html_text = f'<dl>{_value}</dl>'
    return html_text



definitions = []
print(build_definition_list(definitions))
