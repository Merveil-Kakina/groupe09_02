"""
Énoncé :
Écrire un programme qui demande deux nombres à l’utilisateur et affiche :
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
