import pandas as pd
from pandas import ExcelWriter

import numpy as np
#import matplotlib.pyplot as plt
import datetime
from urllib.parse import urlparse
import hashlib
# librerias propias
# libreria para leer desde main.py
import ETL.data_analysis.utils.delword as dlw
import ETL.data_analysis.utils.top_word as tw

"""
#Para trabajar en local
import utils.delword as dlw
import utils.top_word as tw
 """


def save_data(df_data,today):
    df_data.to_csv(f'data/{today}/data_transform.csv', sep=',')
    writer = ExcelWriter(f'data/{today}/data_transform.xlsx')
    df_data.to_excel(writer, 'Hoja de datos', index=False)
    writer.save()


def top_words_c(df_data):
    words_contents = list(df_data.apply(
        lambda row: dlw.delword(row['contents']), axis=1)) # se convierte en una lista
    token_contents = []
    top_words_1_contents = []
    top_words_2_contents = []
    top_words_3_contents = []
    #print(words_contents)
    for i in words_contents:
        token_contents.append(len(i))
        #print(i)
        top_words = tw.top_word(i)[:3]
        #print(top_words)

        top_words_1_contents.append(top_words[0])
        top_words_2_contents.append(top_words[1])
        top_words_3_contents.append(top_words[2])

    #print(top_words_3_contents)
    return token_contents, top_words_1_contents, top_words_2_contents, top_words_3_contents


def data_wrangling(df_data):
    #eliminar la fila con title que no sean el encabezado
    df_idx=df_data[df_data["title"]=="title"].index
    df_data=df_data.drop(df_idx)
    #eliminar columna de numeros
    """ if df_data['']:
        df_data.drop([''], axis=1) """
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
    # token o palabras mas relevantes por titulo (el token es la cantidad de palabras relevantes)
    token_title = df_data.apply(lambda row: len(
        dlw.delword(row['title'])), axis=1)
    df_data['token title'] = token_title
    #eliminar la fila con filas de token iguales a 1
    #print(df_data)
    # token o palabras mas relevantes para el contenido y palabras relebantes
    token_contents, top_words_1_contents, top_words_2_contents, top_words_3_contents = top_words_c(
        df_data)
    df_data['token contents'] = token_contents
    df_data['top 1 words contents'] = top_words_1_contents
    df_data['top 2 words contents'] = top_words_2_contents
    df_data['top 3 words contents'] = top_words_3_contents
    ###
    df_idx=df_data[df_data["top 1 words contents"]==0].index
    df_data=df_data.drop(df_idx)
    # devolvemos la data
    return df_data


def read_data(today):
    direccion = f'.\\data\\{today}\\data_extracted.csv'
    df_data = pd.read_csv(direccion)
    return df_data


def transform_data(today):
    # Leer la data
    df_data = read_data(today)
    df_data_mod = data_wrangling(df_data)
    save_data(df_data_mod,today)
    # print(df_data_mod)

# transform_data()
