# du_13.01.26_vytvorenie jednoduchého systému pre správu knižničných zdrojov

class Kniha:
    def __init__(self, nazov, autor, isbn, dostupna, rok_vydania):
        self.nazov = nazov
        self.autor = autor
        self.isbn = isbn
        self.dostupna = dostupna
        self.rok_vydania = rok_vydania

    def vypozicat(self):
        if self.dostupna:
            self.dostupna = False
            print(f"Kniha {self.nazov} je vypožičaná.")
        else:
            print(f"Kniha {self.nazov} nie je dostupná.")

    def vratit(self):
        self.dostupna = True
        print(f"Kniha {self.nazov} je vrátená.")


class Kniznica:
    def __init__(self):
        self.zoznam_knih = []

    def pridaj_knihu(self, kniha):
        self.zoznam_knih.append(kniha)

    def vyhladaj_podla_nazvu(self, nazov):
        for kniha in self.zoznam_knih:
            if kniha.nazov == nazov:
                print(f"Nájdená kniha: {kniha.nazov}")
                return
        print("Kniha sa nenašla.")

    def vypozicat_knihu(self, isbn):
        for kniha in self.zoznam_knih:
            if kniha.isbn == isbn:
                kniha.vypozicat()
                return
        print("Kniha sa nenašla.")

    def vratit_knihu(self, isbn):
        for kniha in self.zoznam_knih:
            if kniha.isbn == isbn:
                kniha.vratit()
                return
        print("Kniha sa nenašla.")

    def zobraz_dostupne_knihy(self):
        for kniha in self.zoznam_knih:
            if kniha.dostupna:
                print(f"Názov: {kniha.nazov}, Autor: {kniha.autor}, ISBN: {kniha.isbn}")


kniznica_ = Kniznica()

kniha1 = Kniha("A Trail Through Time", "Jodi Taylor", "9781472264428", True, 2019)
kniha2 = Kniha("The Hero of Ages", "Brandon Sanderson", "9780575089945", True, 2010)

kniznica_.pridaj_knihu(kniha1)
kniznica_.pridaj_knihu(kniha2)

print("Dostupné knihy:")
kniznica_.zobraz_dostupne_knihy()

