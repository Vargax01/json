# -*- coding: utf-8 -*-
import json
with open('contaminacion.json') as data_file:
    data = json.load(data_file)
print "Monóxido de nitrógeno"
print "Dióxido de nitrógeno"
print "Partículas en suspensión PM10"
print "Ozono"
print "Tolueno"
print "Benceno"
print "Xileno"
print "Hidrocarburos totales"
print "Hidrocarburos no metano"
dato=str(raw_input("Dame un dato: "))
fecha=str(raw_input("Dame un año para hacer la media de ese dato(2000-2017): "))
dato=dato.decode('utf-8')
cont=0
suma=0
for elem in data:
    if elem["Fecha"].split("-")[0] == fecha:
        for elem1 in elem:
            if elem1 == dato and elem[elem1] != None:
                suma=suma+elem[elem1]
            elif elem1 == dato and elem[elem1] == None:
                suma=suma+0
        cont=cont+1
resultado=suma/float(cont)
print "La media del dato", dato, "en el año", fecha, "es", resultado