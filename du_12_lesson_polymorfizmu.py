# du_13_01_2026 polymorfizmu

class Tvar:
    def obsah(self):
        print("vypocet obsahu")

class Obdlznik(Tvar):
    def obsah(self):
        print("obdlznik")

class Kruh(Tvar):
    def obsah(self):
        print("kruh")

class Pravouhly_trojuholnik(Tvar):
    def obsah(self):
        print("pravouhly trojuholnik")

tvary = [Obdlznik(), Kruh(), Pravouhly_trojuholnik()]

for i in range(3):
    tvary[i].obsah()


