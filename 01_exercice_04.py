#Exercice 4
"""
Énoncé :
Demander une note sur 20 et afficher la note sur 100.
"""

class NoteSur100:
    def __init__(self, note20):
        self.note20 = note20
    def note100(self):
        note100 = (self.note20 / 20) * 100
        print(f"Note sur 100 : {note100:.2f}")
if __name__ == "__main__":
    note20 = float(input("Note20 : "))
    obj = NoteSur100(note20)
    obj.note100()
