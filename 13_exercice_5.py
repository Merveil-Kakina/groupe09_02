#Exercice 5 — Manipulation avancée avec finally
"""
Énoncé :
Demander un nombre et calculer sa racine carrée.
Afficher un message final quelle que soit l’issue.
"""

class RacineFinal:
    def __init__(self, nombre):
        self.nombre = nombre
    def calculer(self):
        import math
        try:
            print(math.sqrt(self.nombre))
        finally:
            print('Fin du programme')
if __name__ == "__main__":
    nombre = int(input('Nombre : '))
    obj = RacineFinal(nombre)
    obj.calculer()
