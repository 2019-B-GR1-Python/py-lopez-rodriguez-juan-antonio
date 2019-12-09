# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 23:45:58 2019

@author: juanc
"""
import pandas as pd
import numpy as np
# importar sistema operativo
import os
import sqlite3
import xlsxwriter
import matplotlib.pyplot as plt
import seaborn as sns

# path = "C://Users//juanc//source//repos//Python//Pandas//DatasetProyecto//original//googleplaystore.csv"

columnas = ['App','Category','Rating',
            'Size','Installs','Type',
            'Price','Content Rating']

# leer del original
# df = pd.read_csv(path, usecols = columnas)

#GUARDAR COPIA
path_guardado_pickle = "C://Users//juanc//source//repos//Python//Pandas//DatasetProyecto//googleplaystore_saved.pickle"
#df.to_pickle(path_guardado_pickle)

path_guardado_xlsx = 'C://Users//juanc//source//repos//Python//Pandas//DatasetProyecto//googleplaystore_saved.xlsx'


#leer el excel del original tratado
df1 = pd.read_excel(path_guardado_xlsx)
df1.to_excel(path_guardado_xlsx, index = False) #Guardar excel

#ver columnas
print(list(df1))
df1.columns = ['Unique Value', 'App', 'Category', 'Rating', 'Size', 'Installs', 'Type', 'Price', 'Content Rating']


### informe con multiples hojas de trabajo ###

path_informe = 'C://Users//juanc//source//repos//Python//Pandas//DatasetProyecto//informe.xlsx'
writer = pd.ExcelWriter(path_informe, engine='xlsxwriter')  #instancia de writer

df1.to_excel(writer, sheet_name = 'Original', index = False)

num_juegos = df1['App'].value_counts()
num_juegos.to_excel(writer, sheet_name = 'Numero de versiones por juego')
writer.save()

tamanio_medio = df1['Size'].mean()
calificacion_media = df1['Rating'].mean()

estadisticas = {'Tamanio Promedio': tamanio_medio,
                'Promedio de calificacion': calificacion_media
                }

datos_generales = pd.DataFrame(estadisticas, index = [1])


print(df1['Category'].value_counts())

#pivote de instalaciones por categorias
pivot_cat = pd.pivot_table(df1, index=['Category'], values=['Installs'], aggfunc=np.sum)
instalacion_categoria = pivot_cat.sort_values(by = 'Installs', ascending=False)

#mejor calificacion por categoria
rat = df1[['Rating', 'App', 'Category']]
mejor_calificacion_por_categoria =rat.sort_values(by = 'Rating', ascending = False)


# mas descargadas

columnas2 = ['App','Rating','Installs']
print(df1[columnas2].sort_values(by = 'Installs', ascending=False))


mas_puntuacion = df1[columnas2].sort_values(by = 'Rating', ascending=False)



#GUARDANDO EN EL INFORME


writer = pd.ExcelWriter(path_informe, engine='xlsxwriter')  #instancia de writer
#HOJA 1 ORIGINAL
df1.to_excel(writer, sheet_name = 'Original', index = False)
#HOJA VERSIONES
num_juegos = pd.read_excel(path_informe, sheet_name = 'Numero de versiones por juego') 
num_juegos.columns = ['App', 'Versiones']
num_juegos.to_excel(writer, sheet_name = 'Numero de versiones por juego', index = False)

pivote_instalaciones_por_categoria = pd.pivot_table(df1, index=['Category', 'App'], values = 'Installs', aggfunc = np.sum)
pivote_instalaciones_por_categoria.to_excel(writer, sheet_name = 'Descargas')

columnas3 = ['App', 'Installs']
mas_descargadas = df1[columnas3].sort_values(by = 'Installs', ascending=False)
mas_descargadas.to_excel(writer, sheet_name = 'Top descargas', index = False)

pivot_versiones = pd.pivot_table(df1, index=['Content Rating', 'Category'], values=['Rating'], columns=['Type'], aggfunc='count')
pivot_versiones.fillna(0, inplace=True)
pivot_versiones.to_excel(writer, sheet_name = 'App pagadas y libres por edad')


datos_generales.to_excel(writer, sheet_name = 'Observaciones generales', index = False)

instalacion_categoria.to_excel(writer, sheet_name = 'Instalaciones por categorias')


mejor_calificacion_por_categoria.to_excel(writer, sheet_name = 'Calificacion x categoria', index = False)


#colores
hoja_numero_versiones = writer.sheets['Numero de versiones por juego']
rango_celdas = 'B2:B{}'.format(len(num_juegos.index) + 1)
formato_num_ver = {
        "type": "2_color_scale",
        "min_value": "1",
        "max_value": "2"}
hoja_numero_versiones.conditional_format(rango_celdas, formato_num_ver)

hoja_descargas = writer.sheets['Descargas']
rango_celdas1 = 'C3:C{}'.format(len(num_juegos.index) + 1)
formato_desc = {
        "type": "3_color_scale",
        "min_value": "1",
        "max_value": "10000000"}
hoja_descargas.conditional_format(rango_celdas1, formato_desc)

hoja_topdescargas = writer.sheets['Top descargas']
rango_celdas2 = 'B2:B{}'.format(len(num_juegos.index) + 1)
formato_topdesc = {
        "type": "3_color_scale",
        "min_value": "1",
        "max_value": "10000000"}
hoja_topdescargas.conditional_format(rango_celdas2, formato_topdesc)

hoja_payfree = writer.sheets['App pagadas y libres por edad']
rango_celdas3 = 'C4:C{}'.format(len(num_juegos.index) + 1)
formato_pf = {
        "type": "3_color_scale",
        "min_value": "1",
        "max_value": "500"}
hoja_payfree.conditional_format(rango_celdas3, formato_pf)

hoja_payfree2 = writer.sheets['App pagadas y libres por edad']
rango_celdas32 = 'D4:D{}'.format(len(num_juegos.index) + 1)
formato_pf2 = {
        "type": "3_color_scale",
        "min_value": "1",
        "max_value": "500"}
hoja_payfree2.conditional_format(rango_celdas32, formato_pf2)


hoja_inst_cat = writer.sheets['Instalaciones por categorias']
rango_celdas4 = 'B2:B{}'.format(len(num_juegos.index) + 1)
formato_pf4 = {
        "type": "3_color_scale",
        "min_value": "1",
        "max_value": "500"}
hoja_inst_cat.conditional_format(rango_celdas4, formato_pf4)

hoja_cal_cat = writer.sheets['Calificacion x categoria']
rango_celdas5 = 'A2:A{}'.format(len(num_juegos.index) + 1)
formato_pf5 = {
        "type": "3_color_scale",
        "min_value": "1",
        "max_value": "5"}
hoja_cal_cat.conditional_format(rango_celdas5, formato_pf5)



writer.save();



# GRAFICOS
#instalaciones x categorias (mas descargados)
instalacion_categoria.plot(kind = 'bar', legend = 'Reverse')
plt.xlabel('Categorias')
plt.ylabel('Instalaciones')

#mas descargados
mas_descargadasg = mas_descargadas.iloc[0:10]
print(list(mas_descargadasg['App']))
mas_descargadasg.index = ['Subway Surfers', 'Facebook', 'Messenger – Text and Video Chat for Free', 'Google Drive', 'Google Drive', 'Google Photos', 'YouTube', 'Google Photos', 'Skype - free IM & video calls', 'Google Play Movies & TV']
mas_descargadasg.plot(kind = 'bar', legend = 'Reverse')
plt.xlabel('Aplicaciones')
plt.ylabel('Descargas')
#mas descargados2
mas_descargadasg2 = mas_descargadas.iloc[10:20]
print(list(mas_descargadasg2['App']))
mas_descargadasg2.index = ['Google Photos', 'Google Drive', 'Hangouts', 'Google', 'Google Play Books', 'Google+', 'Messenger – Text and Video Chat for Free', 'Maps - Navigate & Explore', 'Gmail', 'Google News']
mas_descargadasg2.plot(kind = 'bar', legend = 'Reverse')
plt.xlabel('Aplicaciones')
plt.ylabel('Descargas')




#versiones por juego 1
num_juegosg = num_juegos.iloc[0:10]
num_juegosg.index = ['ROBLOX', 'CBS Sports App - Scores, News, Stats & Watch Live', '8 Ball Pool', 'ESPN', 'Duolingo: Learn Languages Free', 'Candy Crush Saga', 'Zombie Catchers', 'slither.io', 'Helix Jump', 'Nick']
num_juegosg.plot(kind = 'bar', legend = 'Reverse')
plt.xlabel('Juegos')
plt.ylabel('Versiones')
#versiones por juego 2
num_juegosg2 = num_juegos.iloc[10:20]
print(list(num_juegosg2['App']))
num_juegosg2.index = ['Bowmasters', 'Subway Surfers', 'Sniper 3D Gun Shooter: Free Shooting Games - FPS', 'Temple Run 2', 'Bleacher Report: sports news, scores, & highlights', 'Bubble Shooter', 'Flow Free', 'Wish - Shopping Made Fun', 'Angry Birds Classic', 'TripAdvisor Hotels Flights Restaurants Attractions']
num_juegosg2.plot(kind = 'bar', legend = 'Reverse')
plt.xlabel('Juegos')
plt.ylabel('Versiones')


#pagadas libres
pivot_versiones.groupby('Content Rating').plot(kind = 'bar', legend = 'Reverse')
plt.xlabel('Categorias')
plt.ylabel('Instalaciones')


print(pivot_versiones)






