# du_13_01_2026 polymorfizmu

# riešenie 1

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


# riešenie 2

class Tvar:
    def obsah(self):
        print("vypocet obsahu")

class Obdlznik(Tvar):
    def obsah(self):
        print("obdlznik:")
        print("s = a * b")
        print()

class Kruh(Tvar):
    def obsah(self):
        print("kruh:")
        print("s = 3.14 * r ** 2")
        print()

class Pravouhly_trojuholnik(Tvar):
    def obsah(self):
        print("pravouhly trojuholnik:")
        print("s = (a * b) / 2")
        print()


tvary = [Obdlznik(), Kruh(), Pravouhly_trojuholnik()]

for i in range(3):
    tvary[i].obsah()