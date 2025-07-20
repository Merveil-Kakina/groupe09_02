#Exercice 2 — Générateur de statistiques
"""
Énoncé :
Écrire une fonction qui prend une liste de nombres et retourne la somme, la moyenne et le 
maximum.
"""

class GenerateurStats:
    def __init__(self, liste):
        self.liste = liste
    def generer(self):
        print(sum(self.liste), sum(self.liste)/len(self.liste), max(self.liste))
if __name__ == "__main__":
    liste = input('Liste : ')
    obj = GenerateurStats(liste)
    obj.generer()
