"""Énoncé :
Demander trois notes (sur 20), calculer la moyenne et dire si l’étudiant est reçu (moyenne ≥ 10) ou non.
"""


class MoyenneNotes:
    def __init__(self, notes):
        self.notes = notes
    def calculer(self):
        moy = sum(self.notes) / len(self.notes)
        etat = "Reçu" if moy >= 10 else "Non reçu"
        print(f"Moyenne : {moy:.2f}, {etat}")
if __name__ == "__main__":
    notes = input("Notes : ")
    obj = MoyenneNotes(notes)
    obj.calculer()
