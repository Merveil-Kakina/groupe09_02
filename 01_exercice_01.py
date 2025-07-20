#Exercice 1

"""
Énoncé :
Créer un programme qui demande le prénom, l’âge, la ville et le métier d’un utilisateur, puis 
affiche un mini profil structuré.
Ensuite, ajouter une conversion d'âge en nombre de jours vécus (approximation).
Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"""

class ProfilUtilisateur:
    def __init__(self, prenom, age, ville, metier):
        self.prenom = prenom
        self.age = age
        self.ville = ville
        self.metier = metier
    def jours_vecus(self):
        jours = self.age * 365
        print(f"Profil : {self.prenom}, {self.age} ans (~{jours} jours), {self.ville}, {self.metier}")
if __name__ == "__main__":
    prenom = input("Prenom : ")
    age = int(input("Age : "))
    ville = input("Ville : ")
    metier = input("Metier : ")
    obj = ProfilUtilisateur(prenom, age, ville, metier)
    obj.jours_vecus()
