import pandas as pd

tablaSiembras=pd.read_csv('./Siembras.csv')

# filtro 1. Datos por municipio:
# Andes
# Barbosa
# Caldas
# Tamesis
# Yamuramal

tablaDatosMunicipios=tablaSiembras[(tablaSiembras["Ciudad"]=="Andes")|(tablaSiembras["Ciudad"]=="Barbosa")|(tablaSiembras["Ciudad"]=="Caldas")|(tablaSiembras["Ciudad"]=="Tamesis")|(tablaSiembras["Ciudad"]=="Yarumal")]
#print(tablaDatosMunicipios.to_string())


archivoHTML=tablaDatosMunicipios.to_html()
archivoTEXTO=open("datosMunicipios.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
