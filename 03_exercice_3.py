#Exercice 3 — Calculateur de frais de livraison
"""
Énoncé :
Demander la valeur d'un panier. Si le montant est :
• ≥ 1️00 € → Livraison gratuite.
• Entre 5️0 € et 99.99 € → Livraison 5️ €.
• < 5️0 € → Livraison 1️0 €.
Afficher le total à payer (panier + livraison).
"""

class CalculateurFacture:
    def __init__(self, ht, tva):
        self.ht = ht
        self.tva = tva
    def calculer_ttc(self):
        ttc = self.ht * (1 + self.tva / 100)
        print(f"Montant TTC : {ttc:.2f} €")
if __name__ == "__main__":
    ht = float(input("Ht : "))
    tva = float(input("Tva : "))
    obj = CalculateurFacture(ht, tva)
    obj.calculer_ttc()
