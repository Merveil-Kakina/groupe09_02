# Générer une liste de carrés et filtrer*

"""
Énoncé :
Créer une liste de carrés pour les nombres de 1 à 20, puis afficher uniquement ceux supérieurs à 100.
"""


class FiltrerCarres:
    def __init__(self, max_val):
        self.max_val = max_val
    def filtrer(self):
        carrés = [i*i for i in range(1, self.max_val+1)]
        print([x for x in carrés if x > 100])
if __name__ == "__main__":
    max_val = int(input("Max_val : "))
    obj = FiltrerCarres(max_val)
    obj.filtrer()
