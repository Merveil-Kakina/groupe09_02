#Exercice 4 — Mot de passe jusqu’à réussite
""""
Énoncé :
Demander un mot de passe à l’utilisateur, continuer à redemander tant qu’il n’est pas correct.
Mot de passe correct = "Python2025".
""""

mdp = " "

while mdp != "Python2025":
    mdp = input("Entrez le mot de passe : ")
    if mdp != "Python2025":
        print("Mot de passe incorrect, réessayez.")

print("Mot de passe correct, accès autorisé.")

