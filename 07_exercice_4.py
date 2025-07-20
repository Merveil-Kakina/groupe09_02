#Exercice 4 — Liste de tuples (étudiants et notes)
"""
Énoncé :
Créer une liste de tuples contenant le nom d’un étudiant et sa note. Afficher tous les étudiants 
ayant une note supérieure ou égale à 15.
"""

etudiants = [("Alice", 16), ("Paul", 14), ("Sara", 18), ("John", 12)]

print("Étudiants avec note >= 15 :")
for nom, note in etudiants:
    if note >= 15:
        print(f"{nom} - {note}")
        

