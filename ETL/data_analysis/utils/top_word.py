from collections import Counter

def top_word(lista):

    count_lista=Counter(lista)
    top_words = count_lista.most_common()
    #first, second, *_, last = count_lista.most_common()
    return top_words