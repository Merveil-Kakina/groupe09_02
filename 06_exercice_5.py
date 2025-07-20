#Exercice 5 — Calculer factorielle (sans math.factorial)
"""
Énoncé :
Demander un nombre entier positif et calculer sa factorielle via while.
"""
class CalculFactorielle:
    def __init__(self, n):
        self.n = n

    def calculer(self):
        fact = 1
        for i in range(1, self.n + 1):
            fact *= i
        print(f"Factorielle de {self.n} : {fact}")

if __name__ == "__main__":
    n = int(input("Entrez un entier pour la factorielle : "))
    CalculFactorielle(n).calculer()


