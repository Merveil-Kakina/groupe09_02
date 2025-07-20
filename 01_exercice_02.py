#Exercice 2
"""
Énoncé :
Créer une mini "fiche produit" qui contient nom, prix, stock, remise. Calculer le prix final après 
remise.
"""
class Produit:
    def __init__(self, nom, prix, stock, remise_pct):
        self.nom = nom
        self.prix = prix
        self.stock = stock
        self.remise_pct = remise_pct
    def prix_final(self):
        pf = self.prix * (1 - self.remise_pct / 100)
        print(f"Produit : {self.nom}")
        print(f"  Prix unitaire : {self.prix:.2f} €")
        print(f"  Remise : {self.remise_pct:.1f}%")
        print(f"  Prix final : {pf:.2f} €")
        print(f"  Stock : {self.stock}")
if __name__ == "__main__":
    nom = input("Nom : ")
    prix = float(input("Prix : "))
    stock = int(input("Stock : "))
    remise_pct = float(input("Remise_pct : "))
    obj = Produit(nom, prix, stock, remise_pct)
    obj.prix_final()

