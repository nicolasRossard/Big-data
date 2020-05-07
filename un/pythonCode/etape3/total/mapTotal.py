#!/usr/bin/python
import sys
# Boucle pour recuperer les elements
for line in sys.stdin:
	# Separation des colonnes via la tabulation "\t" 
	# et enregistrement des donnees
	data = line.strip().split("\t")
	# Verification que data possede  elements a savoir:
	# date temps magasin produit cout paiement
	if len(data) == 6:
		# Stockage des donnees
		data, time, store, item, cost, payment = data
		# Affichage de la clef 1 et du cout
		# On veut la vente total de tous les produits dans tous les magasins
		print "{0}\t{1}".format(1,cost)
