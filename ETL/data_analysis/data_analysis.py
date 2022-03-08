import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import datetime
from urllib.parse import urlparse
import hashlib
# Leer la data
today = datetime.date.today().strftime('%d-%m-%y')


def data_wrangling(df_data):
    #separar el host de la url
    df_data['host']=df_data['url'].apply(lambda url: urlparse(url).netloc)
    #eliminiar filas con datos faltantes
    df_data=df_data.dropna(subset=["contents","title"])
    #crear un hash para cada elemento
    uids=(df_data
        .apply(lambda row:hashlib.md5(bytes(row['url'].encode())),axis=1)
        .apply(lambda hash_object: hash_object.hexdigest())
      )
    df_data['uid']=uids
    #devolvemos la data
    print(df_data)

def data(today):
    direccion = f'.\\data\\{today}.csv'
    df_data = pd.read_csv(direccion)
    return df_data

if __name__ == '__main__':

    df_data = data(today)
    data_wrangling(df_data)
