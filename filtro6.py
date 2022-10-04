import pandas as pd

tablaSiembras=pd.read_csv('./Siembras.csv')

#6. Los Datos de la veredas quitasol de bello ordenados de mayor a mejor y el promedio de arboles sembrados en esta vereda
tablaDatosQuitasol= tablaSiembras[(tablaSiembras["Vereda"]=="Quitasol") & (tablaSiembras["Ciudad"]=="Bello") ].sort_values("Arboles")

tablaEstadisticas=tablaDatosQuitasol.describe()

tablaMedias=tablaEstadisticas.loc[['mean']]

tablaMediasArboles= tablaMedias["Arboles"].to_frame()



archivoHTML=tablaDatosQuitasol.to_html()
archivoTEXTO=open("tablaDatosQuitasol.html", "w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

archivoHTML=tablaMediasArboles.to_html()
archivoTEXTO=open("tablaMediasArboles.html", "w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()