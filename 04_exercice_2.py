#Exercice 2 — Gestionnaire d'accès bâtiment
"""
Énoncé :
Demander le rôle (employé, visiteur, sécurité).
Si employé → demander badge valide (oui/non) → accès.
Si visiteur → demander s’il a rendez-vous → accès si oui.
Si sécurité → accès direct.
Sinon → refuser.
"""

class GestionAccesBatiment:
    def __init__(self, role):
        self.role = role
    def verifier(self):
        r = self.role.lower()
        if r == 'employé':
            badge = input("Badge valide (oui/non) : ")
            print("Accès autorisé" if badge.lower() == 'oui' else "Accès refusé")
        elif r == 'visiteur':
            rdv = input("Vous avez un rendez-vous (oui/non) : ")
            print("Accès autorisé" if rdv.lower() == 'oui' else "Accès refusé")
        elif r == 'sécurité':
            print("Accès autorisé")
        else:
            print("Accès refusé")
if __name__ == "__main__":
    role = input("Role : ")
    obj = GestionAccesBatiment(role)
    obj.verifier()
