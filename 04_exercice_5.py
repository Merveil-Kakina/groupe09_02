#Exercice 5 — Simulation de commande restaurant
"""
Énoncé :
Demander le type de plat (viande, poisson, végétarien).
Si viande → demander cuisson (saignant, à point, bien cuit).
Si poisson → demander sauce (citron, beurre).
Si végétarien → proposer salade ou pâtes.
"""
class SimulationCommande:
    def __init__(self, type_plat):
        self.type_plat = type_plat
    def commander(self):
        tp = self.type_plat.lower()
        if tp == 'viande':
            cuisson = input("Cuisson (saignant/à point/bien cuit) : ")
            print(f"Vous avez choisi viande, cuisson : {cuisson}")
        elif tp == 'poisson':
            sauce = input("Sauce (citron/beurre) : ")
            print(f"Vous avez choisi poisson, sauce : {sauce}")
        elif tp == 'végétarien':
            choix = input("Salade ou pâtes ? ")
            print(f"Vous avez choisi végétarien : {choix}")
        else:
            print("Type de plat inconnu")
if __name__ == "__main__":
    type_plat = input("Type_plat : ")
    obj = SimulationCommande(type_plat)
    obj.commander()

