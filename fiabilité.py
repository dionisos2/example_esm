#!/bin/python

print("nombre d’heure par mois")
heure_par_mois = int(input())
print("décalage en mois")
decalage_en_mois = int(input()) + 1
print("nombre de mois de travail")
nombre_de_mois = int(input())

fiabilite = 50
for decalage_courant in range(decalage_en_mois, nombre_de_mois+decalage_en_mois):
    fiabilite += heure_par_mois/decalage_courant

print("fiabilité = " + str(fiabilite));
