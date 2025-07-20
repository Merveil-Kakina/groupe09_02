#Exercice 2 — Système de classification de notes
"""
Énoncé :
Demander une note sur 1️00 et attribuer une mention :
• ≥ 90 : Excellent
• ≥ 75️ : Très Bien
• ≥ 60 : Bien
• ≥ 5️0 : Passable
• < 50 : Insuffisant
"""

class VerifDivisible:
    def __init__(self, n):
        self.n = n
    def verifier(self):
        if self.n % 3 == 0 and self.n % 5 == 0:
            print("Divisible par 3 et 5")
        else:
            print("Pas divisible par 3 et 5")
if __name__ == "__main__":
    n = input("N : ")
    obj = VerifDivisible(n)
    obj.verifier()
