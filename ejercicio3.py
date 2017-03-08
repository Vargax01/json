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
numero1=int(raw_input("Dame un número: "))
numero2=int(raw_input("Dame otro número: "))
dato=dato.decode('utf-8')
for elem in data:
    for elem1 in elem:
        if elem1 == dato and elem[elem1]