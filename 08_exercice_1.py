# Parcourir une liste de dictionnaires*

"""Énoncé :
Avoir une liste de dictionnaires représentant des livres (titre, auteur, année). Afficher tous les livres publiés après 2010.
"""

class ParcoursDictionnaires:
    def __init__(self, livres):
        self.livres = livres
    def afficher(self):
        for livre in self.livres:
            if livre['annee'] > 2010: print(livre)
if __name__ == "__main__":
    livres = input('Livres : ')
    obj = ParcoursDictionnaires(livres)
    obj.afficher()
