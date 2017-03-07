# -*- coding: utf-8 -*-
import json
print "Monóxido de nitrógeno"
print "Dióxido de nitrógeno"
print "Partículas en suspensión PM10"
print "Ozono"
print "Tolueno"
print "Benceno"
print "Xileno"
print "Hidrocarburos totales"
print "Hidrocarburos no metano"
listadat=[]
pasa=False
while pasa == False:
    dato=str(raw_input("Dame un dato pulse o pulse q para quitar: "))
    if dato == "q":
        pasa=True
    else:
        listadat.append(dato.decode('utf-8'))


cad_uni='Monóxido de nitrógeno'
with open('contaminacion.json') as data_file:
    data = json.load(data_file)
for elem in data:
    print elem["Fecha"]
    for elem1 in elem:
        if elem1 in listadat:
            print elem1, ":", elem[elem1]
    print "###################################################"
