palabras_comunes = ['de', 'del', 'su', 'se', 'es','ese', 'para', 'la', 'el','le', 'ha', 'a', 'e', 'i', 'o', 'u', 'las', 'al', 'les',
                    'los', 'sus', 'ser', 'y', 'que', 'en', 'un', 'una', 'por', 'al', 'lo', 'hay', 'ahi', 'sin', 'tal', 'vez',
                    'con', 'si', 'no', 'ni', 'este', 'esta', 'estos', 'tras', 'como', 'ya', 'toda', 'estan', 'entre', 'ademas', 'además', 'menos',
                    'también', 'tambien', 'aplica','más','según','está','nos','me','parte','partes','otros','otro','ante','fue','pero']


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
