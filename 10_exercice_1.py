#Exercice 1 — Extraire le milieu d’une chaîne
"""
Énoncé :
Demander un mot d'au moins 5 lettres. Extraire et afficher la partie centrale (sans les 2 premières 
et 2 dernières lettres).
"""
class ExtraireMilieu:
    def __init__(self, mot):
        self.mot = mot
    def extraire(self):
        print(self.mot[2:-2])
if __name__ == "__main__":
    mot = input('Mot : ')
    obj = ExtraireMilieu(mot)
    obj.extraire()
