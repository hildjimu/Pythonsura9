import pandas as pd

tablaSiembras=pd.read_csv('./Siembras.csv')

#6. Los Datos de CARAMANTA
tablaDatosCaramanta= tablaSiembras[(tablaSiembras["Ciudad"]=="Caramanta") ]

#print(tablaDatosCaramanta)

archivoHTML=tablaDatosCaramanta.to_html()
archivoTEXTO=open("tablaDatosCaramanta.html", "w", encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()