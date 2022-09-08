target = ''
def translate(occurence, transpiled):
    global target

    target = target.replace(occurence, transpiled)
    return target
