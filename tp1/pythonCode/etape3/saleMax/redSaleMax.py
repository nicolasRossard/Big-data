#!/usr/bin/python
import sys

saleMax = 0
oldKey = None
for line in sys.stdin:
	# Parcourt les donnees crees par le mapper (magasin,cout)
	# Le nom du magasin est la clef
	data = line.strip().split("\t")

	# Si la longueur des donnees n'est pas la bonne 
	# on passe ce "couple clef,valeur)
	if len(data) !=2:
		continue
	# enregistrement des donnees dans data
	thisKey, thisSale = data
	# print oldKey and oldKey
	# Dans cette partie les donnees sorties par mapper doivent etre triees
	# Sinon cela ne fonctionne pas
	# On regarde si la clef est la meme
	if oldKey and oldKey != thisKey:
		# Si faux
		# On affiche la somme des produits par le magasin
		print "{0}\t{1}".format(oldKey,saleMax)
		# Remise a 0 de la vente totale
		saleMax = 0
	# On met la nouvelle clef
	oldKey = thisKey

	# On compare les deux ventes 
	if float (saleMax) < float (thisSale):
		#si vrai on recupere la vente la plus chere
		saleMax = thisSale

# Affiche la derniere clef si non-nulle
if oldKey != None:
	print oldKey,"\t",saleMax
