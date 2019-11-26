# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:57:33 2019

@author: juanc
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

serie_a = pd.Series(
        lista_numeros)

serie_b = pd.Series(
        tupla_numeros)

serie_c = pd.Series(
        np_numeros)

serie_d = pd.Series([
        True,
        False,
        12,
        12.12,
        "1",
        None,
        (),
        [],
        {"Nombre":"Juan"}])


serie_d[3]

lista_ciudades = ["Ambato",
                  "Cuenca",
                  "Loja",
                  "Quito"]

serie_ciudades = pd.Series(
        lista_ciudades,
        index=[
                "A",
                "C",
                "L",
                "Q",
                ])

serie_ciudades["Q"]
serie_ciudades[3]

valores_ciudad = {
        "Ibarra":9500,
        "Guayaquil":10000,
        "Cuenca":7000,
        "Quito":8000,
        "Loja":3000
        }

serie_valor_ciudad = pd.Series(
        valores_ciudad)

serie_valor_ciudad["Guayaquil"]
serie_valor_ciudad[1]

ciudades_menores_5000 = serie_valor_ciudad < 5000

s5 = serie_valor_ciudad[ciudades_menores_5000]

mas_10porciento = serie_valor_ciudad * 1.10
serie_valor_ciudad = serie_valor_ciudad * 1.10

quito_menos50 = serie_valor_ciudad["Quito"] - 50
serie_valor_ciudad["Quito"]= serie_valor_ciudad["Quito"] - 50


print("Lima" in serie_valor_ciudad)
print("Quito" in serie_valor_ciudad)

respuesta_square = np.square(serie_valor_ciudad)
resp_seno = np.sin(serie_valor_ciudad)


ciudades_uno = pd.Series({
        "Montañita":300,
        "Guayaquil": 10000,
        "Quito":2000})

ciudades_dos = pd.Series({
        "Loja":300,
        "Guayaquil": 10000})

presupuesto_total_uno_y_dos = ciudades_uno + ciudades_dos
# deben ternerse los mismo indices, 
# sino retorna nan cuando no coinciden los inidices

ciudades_uno["Loja"]=0
#se pueden incluir indices

ciudades_dos["Quito"]=0
ciudades_dos["Montañita"]=0


prspt_total_uno_y_dos_bien = ciudades_uno + ciudades_dos

ciu_add = ciudades_uno.add(ciudades_dos)

ciu_concatenadas = pd.concat([ciudades_uno,
                              ciudades_dos])

ciu_concatenadas_v = pd.concat([ciudades_uno,
                              ciudades_dos
                              ], verify_integrity = True)

ciud_append_v = ciudades_uno.append(
        ciudades_dos, verify_integrity = True)

#sacar el valor mayor de la serie
#se puede de dos formas
ciudades_uno.max()
pd.Series.max(ciudades_uno)
np.max(ciudades_uno)


#sacar minimo, dos formas
ciudades_uno.min()
pd.Series.min(ciudades_uno)
np.min(ciudades_uno)

# Estadisticas
ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

#saca los dos primeros
ciudades_uno.head(2)

#saca los dos ultimos
ciudades_uno.tail(2)

#ordena y saca los dos primeros de menor
ciudades_uno.sort_values().head(2)

# el ascending permite ordenar de mayor a menor si esta false
ciudades_uno.sort_values(
        ascending = False).head(2)


ciudades_uno.sort_values().tail(2)


# 0 - 1000 subir un 5%
# 1001 - 5000 subir un 10%
# 5001 - 20000 subir 15%
#FUNCIONES
    
def calculo(valor):
    if(valor <= 1000):
        return valor * 1.05
    if(valor > 1000 and valor <= 5000):
        return valor * 1.10
    if(valor > 5000):
        return valor * 1.15


ciudad_calculada = ciudades_uno.map(calculo)
    
ciudades_uno
ciudad_calculada


# FUNCION WHERE
# se le pasa el valor para cada iteracion, en este caso se utiliza la variable ciudades_uno
# se aplica a los que NO CUMPLEN la condicion
ciudades_uno.where(ciudades_uno > 1000, ciudades_uno * 1.05)

ciudades_uno.where(ciudades_uno < 5000, ciudades_uno * 1.15)






























