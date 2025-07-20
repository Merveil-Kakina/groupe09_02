#Exercice 3 — Vérificateur de palindrome
"""
Énoncé :
Créer une fonction qui vérifie si un mot est un palindrome (ex. "radar").
"""


class VerificateurPalindrome:
    def __init__(self, mot):
        self.mot = mot
    def verifier(self):
        print('Palindrome' if self.mot == self.mot[::-1] else 'Pas palindrome')
if __name__ == "__main__":
    mot = input('Mot : ')
    obj = VerificateurPalindrome(mot)
    obj.verifier()

