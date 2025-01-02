def trim_and_repeat(text, offset=0, repetitions=1):
    return(text[offset:] * repetitions)

text = 'python'

trim_and_repeat(text, offset=3, repetitions=2);  # honhon
trim_and_repeat(text, repetitions=3);  # pythonpythonpython
trim_and_repeat(text) #python