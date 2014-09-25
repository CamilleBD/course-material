# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 11:28:03 2014

@author: sblakeley
"""
station = {
    'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
    'number': 31705,
    'latitude': 48.8645278209514,
    'name': 'CHAMPEAUX (BAGNOLET)',
    'longitude': 2.416170724425901
}
order = ['latitude', 'longitude', 'number', 'name', 'address']
for key in order:
    print(key, station[key])
