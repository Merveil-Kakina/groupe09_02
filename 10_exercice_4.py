#Exercice 4 — Masquer une partie d’un numéro
"""
Énoncé :
Demander un numéro de téléphone (ex. "0897654321"), remplacer tous les chiffres sauf les 3 
derniers par des *.
"""

class MasquerNumero:
    def __init__(self, numero):
        self.numero = numero
    def masquer(self):
        print('*'*(len(self.numero)-3) + self.numero[-3:])
if __name__ == "__main__":
    numero = input('Numero : ')
    obj = MasquerNumero(numero)
    obj.masquer()

