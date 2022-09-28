import pandas as pd

tablaSiembras=pd.read_csv('./Siembras.csv')

# filtro 2. Datos de Medellin ordenados de mayor a menor número de arboles


tablaDatosMedellin=tablaSiembras[(tablaSiembras["Ciudad"]=="Medellín")].sort_values("Arboles", ascending=False)
print(tablaDatosMedellin.to_string())



archivoHTML=tablaDatosMedellin.to_html()
archivoTEXTO=open("datosMedellin.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

