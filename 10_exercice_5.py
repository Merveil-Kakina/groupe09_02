#Exercice 5 — Extraire éléments pairs d’une liste
"""
Énoncé :
Demander une liste de nombres, créer une nouvelle liste contenant uniquement les éléments 
situés aux indices pairs.
"""


class ExtraireIndicesPairs:
    def __init__(self, liste):
        self.liste = liste
    def extraire(self):
        print([self.liste[i] for i in range(0, len(self.liste), 2)])
if __name__ == "__main__":
    liste = input('Liste : ')
    obj = ExtraireIndicesPairs(liste)
    obj.extraire()
