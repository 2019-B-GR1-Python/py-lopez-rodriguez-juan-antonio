# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:49:32 2019

@author: juanc
"""

import pandas as pd


path_guardado_bin = "C://Users//juanc//source//repos//Python//Pandas//data//artwork_data_completo.pickle"
df = pd.read_pickle(path_guardado_bin)

#para ver artistas repetidos
serie_artistas_repetidos = df["artist"]

#para ver artistas sin repetir
artistas = pd.unique(serie_artistas_repetidos)
#para ver cuantos artistas hay
artistas.size
len(artistas)

#solo para ver las obras del artistas blake
blake = df["artist"]=="Blake, William"
#todos los true corresponden a blake
blake.value_counts()

# filtrar solo los datos de blake
#evaluo el dataframe en el archivo booleano de blake
df_blake = df[blake]

























