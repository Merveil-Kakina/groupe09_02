#Exercice 4 — Génération d’acronyme
"""
Énoncé :
Demander un titre ou une phrase, générer un acronyme en prenant la première lettre de chaque 
mot en majuscule.
"""


class GenerateurAcronyme:
    def __init__(self, phrase):
        self.phrase = phrase
    def generer(self):
        acr = ''.join(w[0].upper() for w in self.phrase.split())
        print('Acronyme :', acr)
if __name__ == "__main__":
    phrase = input('Phrase : ')
    obj = GenerateurAcronyme(phrase)
    obj.generer()
