#Exercice 5 — Masquer un mot
"""
Énoncé :
Demander une phrase et un mot. Remplacer ce mot par des astérisques (*)
"""


class MasquerMot:
    def __init__(self, phrase, mot):
        self.phrase = phrase
        self.mot = mot
    def masquer(self):
        res = self.phrase.replace(self.mot, '*'*len(self.mot))
        print(res)
if __name__ == "__main__":
    phrase = input('Phrase : ')
    mot = input('Mot : ')
    obj = MasquerMot(phrase, mot)
    obj.masquer()
