name = input("Imię wolontariusza: ")
sur = input("Nazwisko wolontariusza: ")
nrId = input("Nr Identyfikatora wolontariusza: ")

class Wolontariusz:
    def __init__(self, imie, nazwisko, ID):
        self.imie=imie
        self.nazwisko=nazwisko
        self.ID=ID

wol1 = Wolontariusz(name, sur, nrId)
print (wol1.imie)
