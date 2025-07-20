#Comptage des mots longs*

"""Énoncé :
Demander une phrase à l'utilisateur, afficher le nombre de mots ayant plus de 5 lettres.
"""

class ComptageMotsLongs:
    def __init__(self, phrase):
        self.phrase = phrase
    def compter(self):
        mots = self.phrase.split()
        print(sum(1 for w in mots if len(w) > 5))
if __name__ == "__main__":
    phrase = input('Phrase : ')
    obj = ComptageMotsLongs(phrase)
    obj.compter()
