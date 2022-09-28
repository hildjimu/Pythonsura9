import pandas as pd

tablaSiembras=pd.read_csv('./Siembras.csv')

# filtro 3. Datos de caucasia incluyendo numero de hectarias sembradas. 


tablaDatosCausasia=tablaSiembras[(tablaSiembras["Ciudad"]=="Caucasia")]
tablaDatosCausasia1=tablaDatosCausasia["Hectareas"].to_frame()
#print(tablaDatosCausasia1.to_string())



archivoHTML=tablaDatosCausasia1.to_html()
archivoTEXTO=open("datosCaucasia1.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

