# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:19:33 2020

@author: juanc
"""
import numpy as np
import pandas as pd
import math

path_guardado_bin = "C://Users//juanc//source//repos//Python//Pandas//data//artwork_data_completo.pickle"
df = pd.read_pickle(path_guardado_bin)

seccion_df = df.iloc[49980:50019,:].copy()

df_agrupado = seccion_df.groupby('artist')

type(df_agrupado)



for registros in df_agrupado:
    print(registros)



for columna_agrupada, df_completo  in df_agrupado:
    print(columna_agrupada) #str
    print(df_completo) #dataframe

type(columna_agrupada)
type(df_completo)


# obtener serie con la columna units y ver cuantos hay vacios o no
b = seccion_df['units'].value_counts()
a = seccion_df['depth'].value_counts()
a.empty
b.empty

 

def llenar_valores_vacios(series, tipo):
  lista_valores = series.value_counts()
  if(lista_valores.empty == True):
    return series
  else:
    if(tipo == 'promedio'):
      suma = 0
      cantidad_valores = 0
      for valor_serie in series:
        if(isinstance(valor_serie, str)):
          valor = int(valor_serie)         
          suma = suma + valor
          cantidad_valores = cantidad_valores + 1
        else:
          pass
      promedio = suma / cantidad_valores
      series_valores_llenos = series.fillna(promedio)
      return series_valores_llenos
    
    if(tipo == 'value_counts'):
        mas_repetido = series.value_counts().idxmax()
        
        series_valores_llenos = series.fillna(str(mas_repetido))
        
        return series_valores_llenos
        
# x = serie_u.value_counts().idxmax()           
# y = serie_i.value_counts().idxmax() 
    
def transformar_df(df):
    df_artist = df.groupby('artist')
    lista_df = []
    
    for  artista, df in df_artist:
        copia = df.copy()
        serie_w = copia['width']
        serie_h = copia['height']
        serie_u = copia['units']
        serie_i = copia['inscription']
        # llenar valores con loc y la funcion que se hizo antes
        copia.loc[:,'width'] = llenar_valores_vacios(serie_w, 'promedio')
        copia.loc[:,'height'] = llenar_valores_vacios(serie_h, 'promedio')
        copia.loc[:,'units'] = llenar_valores_vacios(serie_u, 'value_counts')
        copia.loc[:,'inscription'] = llenar_valores_vacios(serie_i, 'value_counts')
        lista_df.append(copia)
        
    df_completo_con_valores = pd.concat(lista_df)
    return df_completo_con_valores

df_valores_llenos = transformar_df(seccion_df)































