#Exercice 1 — Vérificateur complet d'inscription
"""
Énoncé :
Demander l'âge et le pays d'une personne, vérifier si elle peut s’inscrire à un programme :
• Doit avoir au moins 18 ans.
• Doit venir du Congo ou du Cameroun.
• Sinon, message adapté.
"""
class CalculateurArithmetique:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def operations_completes(self):
        print(f"Somme : {self.a + self.b}")
        print(f"Différence : {self.a - self.b}")
        print(f"Produit : {self.a * self.b}")
        print(f"Quotient : {self.a / self.b}")
        print(f"Division entière : {self.a // self.b}")
        print(f"Modulo : {self.a % self.b}")
if __name__ == "__main__":
    a = input("A : ")
    b = input("B : ")
    obj = CalculateurArithmetique(a, b)
    obj.operations_completes()
