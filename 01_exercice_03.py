#Exercice 3
"""
Énoncé :
Écrire un script qui convertit une durée en secondes (entrée sous forme d'heures, minutes, 
secondes).
"""
class ConvertisseurDuree:
    def __init__(self, heures, minutes, secondes):
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes
    def total_secondes(self):
        total = self.heures * 3600 + self.minutes * 60 + self.secondes
        print(f"Durée totale en secondes : {total}")
if __name__ == "__main__":
    heures = int(input("Heures : "))
    minutes = int(input("Minutes : "))
    secondes = int(input("Secondes : "))
    obj = ConvertisseurDuree(heures, minutes, secondes)
    obj.total_secondes()


