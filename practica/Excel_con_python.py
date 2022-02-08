import pandas as pd 
import numpy as np


# para ver un numero concreto de columnas:
pd.set_option("display.max_columns", 20)

df_excel = pd.read_csv("practica\StudentsPerformance.csv")
#print(df_excel)

#sum, max, min, average, count
#print(df_excel.describe())      #solo para datos numericos
#print(df_excel.sum())
#print(df_excel.max())
#print(df_excel.mean())
#print(df_excel.count())

#por filas
#print(df_excel.sum(axis = 1))
#sumamos los valores de dos columnas
#print(df_excel["math score"]+df_excel["reading score"]+df_excel["writing score"]) 

#contamos los valores para el genero masculino y femenino
#print(df_excel["gender"].value_counts())
#====================================================================================

#Creamos nueva columna con la operación de media
df_excel["average"] = np.mean(df_excel, axis=1)

#Creamos nueva columna con la operación con condicional if para saber si se aprueba
df_excel["Pass/Fail"] = np.where(df_excel["average"] > 70, "Pass", "Fail")

#imprimimos
print(df_excel)

#multiple if conditions
conditions = [
    (df_excel["average"]>=90),
    (df_excel["average"]>=80) & (df_excel["average"]<90),
    (df_excel["average"]>=70) & (df_excel["average"]<80),
    (df_excel["average"]>=60) & (df_excel["average"]<70),
    (df_excel["average"]>=50) & (df_excel["average"]<60),
    (df_excel["average"]<50),
]

values = ["A", "B", "C", "D", "E", "F"]
df_excel["grades"] = np.select(conditions, values)
print(df_excel)