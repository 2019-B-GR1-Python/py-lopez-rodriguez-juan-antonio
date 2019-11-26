# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:22 2019

@author: juanc
"""
import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

#DATAFRAME
df1 = pd.DataFrame(arr_pand)

# a partir del Dataframe se crean series
s1 = df1[0]
s2 = df1[1]
s3 = df1[2]

#crear nueva columna, se le iguala el nuevo indice a una nueva serie
df1[3] = s1

# se pueden multiplicar y guardar series
df1[4] = s1 * s2

# dataframe con el arreglo arr_pand, y con indices en las columnas
datos_fisicos_uno = pd.DataFrame(
        arr_pand, columns=['Estatura (cm)',
                           'Peso (kg)',
                           'edad (anios)'])

# con indices
datos_fisicos_dos = pd.DataFrame(
        arr_pand, columns=['Estatura (cm)',
                           'Peso (kg)',
                           'edad (anios)'],
                           index = ['Adrian', 'Vicente'])

# setear o cambiar los indices
df1.index = ['Adrian', 'Vicente']

# setear o cambiar los indices
df1.columns = ['A','B','C','D','E',]









