# Enregistrer statistiques*

"""Énoncé :
Demander une liste de notes, calculer la moyenne et sauvegarder le résultat dans un fichier.
"""

class StatsFichier:
    def __init__(self, notes):
        self.notes = notes
    def enregistrer(self):
        with open('stats.txt', 'w') as f: f.write(f'Moyenne: {sum(self.notes)/len(self.notes)}\n')
if __name__ == "__main__":
    notes = input('Notes : ')
    obj = StatsFichier(notes)
    obj.enregistrer()



