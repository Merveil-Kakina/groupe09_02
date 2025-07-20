#Générer un fichier de table de multiplication*

"""Énoncé :
Demander un nombre et créer un fichier contenant sa table de multiplication (1 à 12).
"""

class TableDansFichier:
    def __init__(self, nombre):
        self.nombre = nombre
    def generer(self):
        with open('table.txt', 'w') as f:
            for i in range(1, 13): f.write(f'{self.nombre} x {i} = {self.nombre*i}\n')
if __name__ == "__main__":
    nombre = int(input('Nombre : '))
    obj = TableDansFichier(nombre)
    obj.generer()
