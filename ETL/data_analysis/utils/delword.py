palabras_comunes = ['de', 'del', 'su', 'se', 'es', 'ese', 'esa','esas','para', 'la', 'el', 'le', 'ha','han', 'a', 'e', 'i', 'o', 'u', 'las',  'les',
                    'los', 'sus', 'ser', 'y', 'que', 'en', 'un', 'una', 'por', 'al', 'lo', 'hay', 'ahi', 'sin', 'tal', 'vez',
                    'con', 'si', 'no', 'ni','son','r', 'este', 'esta', 'estos', 'tras', 'como', 'ya', 'toda', 'estan', 'entre', 'ademas', 'además', 'menos',
                    'también', 'tambien', 'aplica', 'más', 'según', 'está', 'nos', 'me', 'parte', 'partes', 'otros', 'otro', 'ante', 'fue', 
                    'pero', 'va', 'casos', 'uno','dos','tres','cuarto','quinto','cual','the','hasta','será','']


def delword(p):

    p = p.replace(".", '')
    p = p.replace(":", '')
    p = p.replace('"', '')
    p = p.replace('[', '')
    p = p.replace(']', '')
    p = p.replace('«', '')
    p = p.replace('»', '')
    p = p.replace('(', '')
    p = p.replace(')', '')
    p = p.replace('-', '')
    p = p.replace("\xa0", '')
    p = p.replace(" ", ',')
    p = p.lower()
    contents = p.split(',')
    leng_c = len(contents)
    relevant_words = []
    for word in contents:
        if word in palabras_comunes:
            pass
        else:
            relevant_words.append(word)
    return relevant_words

