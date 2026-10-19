import pandas as pd
empleados=[ "Juan Perez","Luis Mendoza", "Cristhian Marques","Juan Perez"]

df=pd.DataFrame({
    "empleados":[ "Juan Perez","Luis Mendoza", "Cristhian Marques","Juan Perez"]
})
print(df.drop_duplicates())
print("-----------------------")

#Normalizacion de etexto
df["empleados_minuscula"]= df["empleados"].str.strip().str.lower()
print(df)
print("-------------------")
#Correcion de tipeo


from rapidfuzz import process
df1=pd.DataFrame({
    "empleados":[ "anaaa","pedro", "lui"]})
lista_valida = ["ana", "pedro", "luis"]

df1["nombre_corregido"]=df1["empleados"].apply(lambda x: process.extractOne(x, lista_valida) [0])

print(df1)
print("-----------------------")
#Unificación de convenciones
df2 = pd.DataFrame(
    {"fecha": ["2026/09/13", "13-09-2026", "Sept 13, 2026"]}
)
df2["fecha"] = pd.to_datetime(df2["fecha"], errors="coerce", format="mixed", dayfirst=True)
print(df2)

print("-----------------------")
#Unificación de decimales

df3 = pd.DataFrame({ "precio": ["10,99", "12,80", "45,55"]})
df3["precio2"] =( df3["precio"].str.replace(",",".").astype(float))

print(df3)

## Eliminación de registros


df4 = df4.dropna()

## Imputación con media
df4["columna"]= df4["columna"].fillna(df4 ["columna"] .mean () )

## Imputación con mediana
df4["columna"]=df4["columna"].fillna(df4["columna"].median () )

## Imputación con moda
df4["columna"] = df4["columna"].fillna (df4 ["columna"] .mode ( ) [0])

## Imputar con algun valor personalizado
print(df4["columna"].fillna (1.0) )
## Imputar con el maximo
print(df4["columna"].fillna(df4["columna"].max () ) )
## Imputar con el minimo")
print(df4["columna"].fillna(df4["columna"].min () ))