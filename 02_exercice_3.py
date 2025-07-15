"""
Énoncé : 
Créer un petit "calculateur de facture" : demander à l’utilisateur un montant HT et un taux de TVA, calculer et afficher le montant TTC.
"""

montant_ht = float(input("Montant HT (€) : "))
taux_tva = float(input("Taux de TVA (%) : "))

#Conversion en coefficient multiplicateur
taux_coef = taux_tva / 100

#Calcul final
montant_ttc = montant_ht * (1 + taux_coef)

print(f"Montant TTC : {montant_ttc:.2f} €")
