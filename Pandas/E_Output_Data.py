# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:57:41 2019

@author: juanc
"""

import pandas as pd
import numpy as np
# importar sistema operativo
import os
import sqlite3


path_guardado_bin = "C://Users//juanc//source//repos//Python//Pandas//data//artwork_data_completo.pickle"
# LEER ARCHIVOS PICKLE
df5 = pd.read_pickle(path_guardado_bin)
df = df5.iloc[49980:50519,:].copy()

#TIPOS DE ARCHIVOS (PARA GUARDAR, EXPORTAR)
#JASON
#EXCEL
#SQL

path_guardado = 'C://Users//juanc//source//repos//Python//Pandas//data//mi_df_completo.xlsx'
###  EXCEL ###
df.to_excel(path_guardado) #Guardar
df.to_excel(path_guardado, index=False) #Guardar sin los indices que estaban

#seleccionar solo las columnas que deseo
columnas = ['artist','title','year']
df.to_excel(path_guardado, columns = columnas)
df.to_excel(path_guardado, index=False,columns = columnas)


### escribir multiples hojas de trabajo ###

path_multiple = 'C://Users//juanc//source//repos//Python//Pandas//data//mi_df_multiples.xlsx'
writer = pd.ExcelWriter(path_multiple, engine='xlsxwriter')  #instancia de writer

#hojas
#sheet_name es para el nombre de la hoja
df.to_excel(writer, sheet_name = 'Primera')

df.to_excel(writer, sheet_name = 'Segunda', index = False)

df.to_excel(writer, sheet_name = 'Tercera', index = False, columns=columnas)

#las hojas hasta aqui solo estan en memoria
# para guardarlas en archivo o sobreescribir se debe enviar al writer
writer.save();




###  Multiples hojas de trabajo ###
# contar artistas
num_artistas = df['artist'].value_counts()
path_colores = 'C://Users//juanc//source//repos//Python//Pandas//data//mi_df_colores.xlsx'

writer = pd.ExcelWriter(path_colores,
                        engine='xlsxwriter')


num_artistas.to_excel(writer, 
                      sheet_name='Artistas')


#la funcion sheets permite seleccionar una hoja
hoja_artistas = writer.sheets['Artistas']


#si no quiero quemar B4 puedo usar variables
#rango_celdas = 'B2:B4'
#se le suma uno para considerar la primera celda que tiene el titulo
rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)


formato_artistas = {
        "type": "3_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"}

#conditional_format recibe rango de celdas y formato, puede tener funciones y todo lo que se desee de excel
hoja_artistas.conditional_format(rango_celdas,
                                 formato_artistas)


writer.save()


# import xlsxwriter

#GRAFICOS
"""
import xlsxwriter

workbook = xlsxwriter.Workbook('C://Users//juanc//source//repos//Python//Pandas//data//mi_df_colores.xlsx')

chart = workbook.add_chart({"type":"line"})
chart.add_series({
        'values':'Artistas!$A$1:$A$6',
        'maker':{
                'type':'square',
                'size':8,
                'border': {'color':'black'},
                'fill': {'color':'red'},
                },
            })

workbook.close()

#Graficos


"""

####################### SQL ############################################
##### IMPORTAR Y EXPORTAR ARCHIVOS SQL CON DBEAVER #####################

with sqlite3.connect("bdd_artist.db") as conexion:
    df5.to_sql('py_artistas', conexion)
    
## with mysql.connect('mysql://user:password@ip:pu')
##  df5.to_sql('tabla_mysql', conexion)




############################### JASON ###############################

df.to_json('artistas.json')



df.to_json('artistas_tabla.json', orient = 'table')

























