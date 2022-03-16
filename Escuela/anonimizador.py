import pandas as pd
import numpy as np
#Funcion para anonimizar los datos sensibles
def anonimizarCol(df,col,palabra_clave):
    for i in range(len(df[col])):
        df[col][i] = palabra_clave + str(i)
    return df

df = pd.read_csv("notas.csv",sep=",")
#Renombramos las columnas a nombres mas sencillos.
df.columns = ["apellido","nombre","levantar_nota","puntaje_extra","p1","p2","p3","p4","p5","total"]
#Anonimizamos
df = anonimizarCol(df,"apellido","lastname")
df = anonimizarCol(df,"nombre","alumno")
#Reemplazamos la columna de String por una booleana
df["levantar_nota"] = np.where(df["levantar_nota"] == "Si", False, True)
#Reemplazamos la coma por el punto.
columnasStr = list(df.select_dtypes("object").columns)
df[columnasStr] = df.select_dtypes("object").apply(lambda x: x.str.replace(',','.'))
#Ahora los tomamos a todos como float
#Lista de columnas que tenemos que cambiar a float
columnas = ["p"+str(i) for i in range(1,6)]
columnas.append("total")
#Ahora transformamos a todas esas columnas a float
df[columnas] = df[columnas].apply(pd.to_numeric)
print("La lista de tipos de datos del dataframe:\n",df.dtypes)
#Finalmente lo escribimos como un csv listo para trabajar
df.to_csv("notas_final.csv", sep=',', encoding='utf-8',index = False)
print("Transformacion de los datos terminada...")

