
#Exercice 1 — Tri manuel d'une liste (sans sort())
"""
Énoncé :
Demander une liste de nombres à l’utilisateur, trier la liste à l’aide de l’algorithme de tri à bulles 
(bubble sort)
"""


class TriBulles:
    def __init__(self, liste):
        self.liste = liste
    def trier(self):
        for i in range(len(self.liste)):
            for j in range(0, len(self.liste)-i-1):
                if self.liste[j] > self.liste[j+1]:
                    self.liste[j], self.liste[j+1] = self.liste[j+1], self.liste[j]
        print('Trié :', self.liste)
if __name__ == "__main__":
    liste = input('Liste : ')
    obj = TriBulles(liste)
    obj.trier()
