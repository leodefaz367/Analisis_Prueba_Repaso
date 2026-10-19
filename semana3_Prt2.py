import pandas as pd
df = pd.read_csv('productos.csv')

print(df.head()) #Primeras filas
print(df.tail()) #ultimas filas
print(df.info()) # Informacion general del dataframe
print(df.describe()) # Estadisticas basicas de columnas numericas
print(df.shape) # Dimensiones filasxcolumnas
print(df.columns) # lista de nombres columnsa
print(df.index) # Índice del DF
print(df.dtypes) # Tipos de datos por columna