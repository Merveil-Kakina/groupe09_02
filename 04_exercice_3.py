#Exercice 3 — Diagnostic de santé simplifié
"""
Énoncé :
Demander si la personne a de la fièvre.
Si oui → demander si elle a des douleurs → "Consulter un médecin".
Si non → demander si elle tousse → "Repos conseillé".
Sinon → "Bonne santé"
"""

class DiagnosticSante:
    def __init__(self, fievre):
        self.fievre = fievre
    def diagnostiquer(self):
        if self.fievre.lower() == 'oui':
            douleurs = input("Douleurs (oui/non) : ")
            print("Consulter un médecin" if douleurs.lower() == 'oui' else "Repos conseillé")
        else:
            tousse = input("Tousse (oui/non) : ")
            print("Repos conseillé" if tousse.lower() == 'oui' else "Bonne santé")
if __name__ == "__main__":
    fievre = input("Fievre : ")
    obj = DiagnosticSante(fievre)
    obj.diagnostiquer()
