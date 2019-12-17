# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:05:01 2019

@author: juanc
"""
import pandas as pd

path_guardado_bin = "C://Users//juanc//source//repos//Python//Pandas//data//artwork_data_completo.pickle"
df = pd.read_pickle(path_guardado_bin)

#obtiene el artista (artist) del index 1035
primero = df.loc[1035, 'artist']

#obtener toda la fila del index 1035
primero = df.loc[1035]

primero = df.iloc[0]

df2 = df.set_index('id')


primero = df2.loc[0]

primero = df2.iloc[0]

#crear un df asi
"""
           nota 1     disciplina
Pepito       7           5
Juanita      8           9
Maria        9           2 
"""

datos = {
        "nota 1": {
                "Pepito":7,
                "Juanita":8,
                "Maria":9},
        "disciplina":{
                "Pepito":5,
                "Juanita":9,
                "Maria":2}
        }

notas = pd.DataFrame(datos)

# en loc se puede filtrar con etiquetas de indice
notas.loc[0] #no vale
notas.loc["Pepito"] #SI vale

# en iloc se puede filtar por el indice
notas.iloc[0] #SI vale
notas.iloc["Pepito"] #NO vale


notas.loc["Pepito","disciplina"]

notas.loc["Pepito",["disciplina","nota 1"]]

notas.loc[["Pepito","Juanita"],"disciplina"]


notas.loc[[True, False, True]]

#notas mayores a 7
condicion_nota = notas["nota 1"] > 7
mayores_a_siete = notas.loc[condicion_nota]
#en una linea s epuede concatenar asi
mayores_a_siete = notas.loc[notas["nota 1"] > 7]

#nota1 mayor7 y disciplina mayor 7
condicion_nota = notas["nota 1"] > 7
condicion_disciplina = notas["disciplina"] > 7

todo_mayor_a_siete = notas.loc[condicion_nota][condicion_disciplina]
#en una sola linea
todo_mayor_a_siete = notas.loc[notas["nota 1"] > 7][notas["disciplina"] > 7]

#setear todas las notas de disciplina como 7
notas.loc["Maria","disciplina"] =7

#EJERCICIOS
#setear 7 a todas las notas menor a 7
notas.loc[notas["disciplina"] < 7] = 7



#Solo a Pepito ponerle 10 en todo
notas.loc["Pepito"] = 10



# PONER 7 E DISCIPLINA A TODOS
notas.loc[:,"disciplina"] = 7

# Aniadir la columna promedio nota 1 y disciplina
#aniado columna promedio
notas["promedio"] = notas.mean([1][0])

#lleno datos promedio



#crear fila con los promedios
notas.loc["promedio"] = notas.mean()




















