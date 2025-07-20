# Parcourir une liste avec `enumerate()`*

"""
Énoncé :
Demander une liste d’éléments et afficher chaque élément avec son indice.
"""


class EnumerateListe:
    def __init__(self, elements):
        self.elements = elements
    def afficher(self):
        for idx, val in enumerate(self.elements): print(idx, val)
if __name__ == "__main__":
    elements = input('Elements : ')
    obj = EnumerateListe(elements)
    obj.afficher()


