import pandas as pd

tablaSiembras=pd.read_csv('./Siembras.csv')

# filtro 5. Los datos de Vereda Rio Arriba y Salazar Herrera


tablaDatosVeredaRAySH=tablaSiembras[(tablaSiembras["Vereda"]=="Rio Arriba") | (tablaSiembras["Vereda"]=="La Salazar")]
print(tablaDatosVeredaRAySH)



archivoHTML=tablaDatosVeredaRAySH.to_html()
archivoTEXTO=open("datoVeredaRAySH.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
