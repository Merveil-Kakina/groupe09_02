#Exercice 4 — Boucle de saisie protégée
"""
Énoncé :
Demander un entier positif (boucle tant que la saisie est invalide).
"""

class SaisieProtegee:
    def __init__(self):
        pass

    def saisir(self) -> int:
        """Demande un entier positif tant que la saisie est invalide."""
        while True:
            try:
                n = int(input("Entier positif : "))
                return n
            except ValueError:
                print("Veuillez entrer un entier valide.")

if __name__ == "__main__":
    valeur = SaisieProtegee().saisir()
    print("Vous avez saisi :", valeur)

