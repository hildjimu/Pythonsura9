import pandas as pd

tablaempleados=pd.read_csv('./empleados.csv')
tablaSiembras=pd.read_csv('./Siembras.csv')

#print(tablaempleados)
#print(tablaempleados.to_string())


#filtro 1 quiero obtener todos los datos de los analistas 1
tablaempleados1=tablaempleados[tablaempleados["cargo"]=="analista1"].head(50)
archivoHTML=tablaempleados1.to_html()

'''
archivoTEXTO=open("datosanalistas1.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''

#filtro 2 quiero obtener todos los datos de los analistas 2
tablaempleados2=tablaempleados[tablaempleados["cargo"]=="analista2"].head(50)
archivoHTML=tablaempleados2.to_html()

'''
archivoTEXTO=open("datosanalistas2.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''

#filtro 3 quiero obtener todos los Analistas <30 años que ganen mas de 5500000
tablaempleados3=tablaempleados[(tablaempleados["salario"]>5500000) & (tablaempleados["edad"]<30)].head(50)

'''
archivoHTML=tablaempleados3.to_html()
archivoTEXTO=open("datosanalistas3.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''



