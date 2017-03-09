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
for elem in data:
    print elem["Fecha"].split("-")[0]
