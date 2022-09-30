import pandas as pd

tablaSiembras=pd.read_csv('./Siembras.csv')

# filtro 4. Los datos de Santa Fe de Antioquia donde se tengan siembras mayores a 250 arboles


tablaDatosSantafeAntioquia=tablaSiembras[(tablaSiembras["Ciudad"]=="Santa Fe de Antioquia") &(tablaSiembras["Arboles"]>250)]
#print(tablaDatosSantafeAntioquia)



archivoHTML=tablaDatosSantafeAntioquia.to_html()
archivoTEXTO=open("datoSantafeAntioquia.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
