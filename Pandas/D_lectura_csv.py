# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:46 2019

@author: juanc
"""
import pandas as pd
# importar sistema operativo
import os

# 1) JSON CSV HTML XML ...
# 2) Binary files -> (!mf-.1234'120))
# Relational Databases 

path = "C://Users//juanc//source//repos//Python//Pandas//data//artwork_data.csv"

df = pd.read_csv(path, nrows = 10)

#columnas que deseo utilizar
columnas = ['id','artist','title',
            'medium','year','acquisitionYear',
            'height','width','units']

df2 = pd.read_csv(path,
                  nrows = 10,
                  usecols = columnas)

df3 = pd.read_csv(path,
                  nrows = 10,
                  usecols = columnas,
                  index_col = 'id')

#GUARDAR DATAFRAME EN ARCHIVOS
#SE CAMBIA LA EXTENSION A .PICKLE
path_guardado = "C://Users//juanc//source//repos//Python//Pandas//data//artwork_data.pickle"

df3.to_pickle(path_guardado)



df4 = pd.read_csv(path)
# guardar binario
path_guardado_bin = "C://Users//juanc//source//repos//Python//Pandas//data//artwork_data_completo.pickle"
df4.to_pickle(path_guardado_bin)

# LEER ARCHIVOS PICKLE
df5 = pd.read_pickle(path_guardado)

























