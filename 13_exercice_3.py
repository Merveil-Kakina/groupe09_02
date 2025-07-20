#Exercice 3 — Lecture de fichier protégée
"""
Énoncé :
Demander un nom de fichier et tenter de l’ouvrir.
Afficher un message si le fichier n’existe pas.
"""

class LectureFichierProtegee:
    def __init__(self, filename):
        self.filename = filename
    def lire(self):
        try:
            with open(self.filename) as f: print(f.read())
        except FileNotFoundError:
            print('Fichier introuvable')
if __name__ == "__main__":
    filename = input('Filename : ')
    obj = LectureFichierProtegee(filename)
    obj.lire()
