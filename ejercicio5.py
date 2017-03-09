# -*- coding: utf-8 -*-
import json
with open('contaminacion.json') as data_file:
    data = json.load(data_file)

dato=str(raw_input("Dame un dato: "))
dato=dato.decode('utf-8')