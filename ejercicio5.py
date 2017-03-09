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
dato=dato.decode('utf-8')
valor=False
print "Fechas en el que", dato, "este en null"
for elem in data:
    for elem1 in elem:
        if elem1 == dato and elem[elem1] == None:
            valor=True
            print elem["Fecha"]

if valor == False:
    print "No hay fechas en el que", dato, "este en null"