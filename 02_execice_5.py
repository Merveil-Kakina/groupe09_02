"""Énoncé :
Écrire un convertisseur de devises qui convertit un montant en dollars vers euros, francs CFA, et livres sterling.  
*Taux* : 1 USD → 0,93 EUR, 1 USD → 610 CFA, 1 USD → 0,79 GBP.
"""


usd = float(input("Montant en USD : "))

eur = usd * 0.93
cfa = usd * 610
gbp = usd * 0.79

print(f"{usd} USD = {eur:.2f} EUR")
print(f"{usd} USD = {cfa:.2f} CFA")
print(f"{usd} USD = {gbp:.2f} GBP")
