"""
Énoncé : 
Demander un nombre entier à l’utilisateur, vérifier s’il est divisible à la fois par 3 et 5, et afficher un message approprié.
"""


n = int(input("Entrez un nombre entier : "))

if n % 3 == 0 and n % 5 == 0:
    print("Le nombre est divisible par 3 et 5.")
else:
    print("Le nombre n’est pas divisible par 3 et 5 en même temps.")
