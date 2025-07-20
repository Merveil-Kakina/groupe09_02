#Exercice 5
"""
Énoncé :
Écrire un programme qui lit une distance (en km) et un temps (en heures), puis calcule la vitesse 
moyenne (km/h) et la vitesse en m/s.
"""
class Vitesse:
    def __init__(self, distance, temps):
        self.distance = distance
        self.temps = temps
    def calculer_vitesse(self):
        v_kmh = self.distance / self.temps
        v_ms = v_kmh * 1000 / 3600
        print(f"Vitesse moyenne : {v_kmh:.2f} km/h, soit {v_ms:.2f} m/s")
if __name__ == "__main__":
    distance = float(input("Distance : "))
    temps = float(input("Temps : "))
    obj = Vitesse(distance, temps)
    obj.calculer_vitesse()
