#Exercice 2 — Filtrage des valeurs uniques
"""
Énoncé :
Demander une liste, puis créer une nouvelle liste contenant uniquement les valeurs uniques (sans 
doublons).
"""


class FiltrerUniques:
    def __init__(self, liste):
        self.liste = liste
    def extraire_uniques(self):
        uniques = []
        for x in self.liste:
            if x not in uniques: uniques.append(x)
        print('Valeurs uniques :', uniques)
if __name__ == "__main__":
    liste = input('Liste : ')
    obj = FiltrerUniques(liste)
    obj.extraire_uniques()

