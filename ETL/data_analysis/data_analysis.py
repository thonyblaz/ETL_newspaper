import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import datetime
from urllib.parse import urlparse
import hashlib
# librerias propias
import utils.delword as dlw
import utils.top_word as tw
# Leer la data
today = datetime.date.today().strftime('%d-%m-%y')


def data_wrangling(df_data):
    # separar el host de la url
    df_data['host'] = df_data['url'].apply(lambda url: urlparse(url).netloc)
    # eliminiar filas con datos faltantes
    df_data = df_data.dropna(subset=["contents", "title"])
    # Para eliminar filas repetidas
    df_data.drop_duplicates(subset=['title'], keep='first', inplace=True)
    # Convertir a minusculas
    df_data['contents'] = df_data.apply(
        lambda row: row['contents'].lower(), axis=1)
    df_data['title'] = df_data.apply(lambda row: row['title'].lower(), axis=1)
    # crear un hash para cada elemento
    uids = (df_data
            .apply(lambda row: hashlib.md5(bytes(row['url'].encode())), axis=1)
            .apply(lambda hash_object: hash_object.hexdigest())
            )
    df_data['uid'] = uids
    # vemos la longitud de cada titulo
    leng_title = df_data.apply(lambda row: len(row['title']), axis=1)
    leng_contents = df_data.apply(lambda row: len(row['contents']), axis=1)
    df_data['leng title'] = leng_title
    df_data['leng contents'] = leng_contents
    # token o palabras mas relevantes por titulo
    token_title = df_data.apply(lambda row: len(
        dlw.delword(row['title'])), axis=1)
    df_data['token title'] = token_title

    # token o palabras mas relevantes para el contenido y palabras relebantes
    words_contents = list(df_data.apply(
        lambda row: dlw.delword(row['contents']), axis=1))
    token_contents = []
    top_words_1_contents = []
    top_words_2_contents = []
    top_words_3_contents = []
    for i in words_contents:
        token_contents.append(len(i))
        top_words =tw.top_word(i)[:3]
        top_words_1_contents.append(top_words[0])
        top_words_2_contents.append(top_words[1])
        top_words_3_contents.append(top_words[2])
    df_data['token contents'] = token_contents
    df_data['top 1 words contents'] = top_words_1_contents
    df_data['top 2 words contents'] = top_words_2_contents
    df_data['top 3 words contents'] = top_words_3_contents

    # devolvemos la data
    print(df_data)


def data(today):
    direccion = f'.\\data\\{today}.csv'
    df_data = pd.read_csv(direccion)
    return df_data


if __name__ == '__main__':

    df_data = data(today)
    data_wrangling(df_data)
