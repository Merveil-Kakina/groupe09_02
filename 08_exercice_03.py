# Liste de listes (tableau 2D)

"""Énoncé : 
Créer une "matrice" 3×3 (liste de listes) et afficher chaque ligne et chaque élément.
"""
class ParcoursMatrice:
    def __init__(self, matrice):
        self.matrice = matrice
    def afficher(self):
        for ligne in self.matrice: print(ligne)
if __name__ == "__main__":
    matrice = input('Matrice : ')
    obj = ParcoursMatrice(matrice)
    obj.afficher()
