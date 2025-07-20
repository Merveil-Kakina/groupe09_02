#Parcourir une chaîne de caractères*

"""Énoncé :
Demander un texte et afficher uniquement les consonnes.
"""

class FiltrerConsonnes:
    def __init__(self, texte):
        self.texte = texte
    def extraire(self):
        cons = ''.join(c for c in self.texte if c.lower() not in 'aeiouy')
        print(cons)
if __name__ == "__main__":
    texte = input('Texte : ')
    obj = FiltrerConsonnes(texte)
    obj.extraire()

