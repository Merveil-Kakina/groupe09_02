#Exercice 3 — Statistiques sur une liste
"""
Énoncé :
Demander une liste de nombres, afficher :
• Maximum
• Minimum
• Moyenne
"""
entree = input("Entrez des nombres : ")
liste = [float(x) for x in entree.split()]

maximum = max(liste)
minimum = min(liste)
moyenne = sum(liste) / len(liste)

print(f"Max : {maximum}")
print(f"Min : {minimum}")
print(f"Moyenne : {moyenne:.2f}")



