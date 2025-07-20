#Exercice 1 — Nettoyer un texte utilisateur
"""
Énoncé :
Demander un texte, retirer tous les espaces en trop (avant et après), convertir en minuscules et 
remplacer tous les points par des points d’exclamation.
"""
class NettoyerTexte:
    def __init__(self, texte):
        self.texte = texte
    def nettoyer(self):
        res = self.texte.strip().lower().replace('.', '!')
        print(res)
if __name__ == "__main__":
    texte = input('Texte : ')
    obj = NettoyerTexte(texte)
    obj.nettoyer()
