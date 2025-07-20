#Exercice 3 — Calcul de moyenne dynamique
"""
Énoncé :
Demander à l’utilisateur d’entrer des notes une par une, arrêter si -1 est saisi.
Calculer et afficher la moyenne finale.
""""



class MoyenneDynamique:
    def __init__(self):
        pass

    def calculer(self):
        notes = []
        while True:
            val = float(input("Note (-1 pour finir) : "))
            if val == -1:
                break
            notes.append(val)
        if notes:
            moy = sum(notes) / len(notes)
            print(f"Moyenne : {moy:.2f}")
        else:
            print("Aucune note saisie.")

if __name__ == "__main__":
    MoyenneDynamique().calculer()

