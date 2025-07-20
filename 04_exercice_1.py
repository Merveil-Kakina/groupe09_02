#Exercice 1 — Calculateur d'abonnement cinéma
"""
Énoncé :
Demander l’âge et la situation (étudiant, salarié, retraité).
Déterminer le tarif :
"""

class CalculateurCinema:
    def __init__(self, age, situation):
        self.age = age
        self.situation = situation
    def calculer(self):
        if self.age < 18: tarif = 5
        elif self.age <= 25 and self.situation.lower() == 'étudiant': tarif = 6
        elif self.age <= 25: tarif = 8
        elif self.situation.lower() == 'retraité': tarif = 7
        else: tarif = 10
        print(f"Tarif cinéma : {tarif} €")
if __name__ == "__main__":
    age = int(input("Age : "))
    situation = input("Situation : ")
    obj = CalculateurCinema(age, situation)
    obj.calculer()
