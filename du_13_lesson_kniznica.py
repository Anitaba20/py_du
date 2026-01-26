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

while True:
    print("\nNavigácia podľa čísla:")
    print("1 Pridať knihu")
    print("2 Vyhľadať knihu podľa názvu")
    print("3 Vypožičať knihu podľa ISBN")
    print("4 Vrátiť knihu podľa ISBN")
    print("5 Zobraziť dostupné knihy")
    print("6 Ukončiť program")

    menu = input("Vyber číslo: ")

    if menu == "1":
        nazov = input("Zadaj názov knihy: ")
        autor = input("Zadaj autora: ")
        isbn = input("Zadaj ISBN: ")
        rok = int(input("Zadaj rok vydania: "))
        nova_kniha = Kniha(nazov, autor, isbn, True, rok)
        kniznica_.pridaj_knihu(nova_kniha)

    elif menu == "2":
        nazov = input("Zadaj názov knihy: ")
        kniznica_.vyhladaj_podla_nazvu(nazov)

    elif menu == "3":
        isbn = input("Zadaj ISBN knihy: ")
        kniznica_.vypozicat_knihu(isbn)

    elif menu == "4":
        isbn = input("Zadaj ISBN knihy: ")
        kniznica_.vratit_knihu(isbn)

    elif menu == "5":
        print("Dostupné knihy:")
        kniznica_.zobraz_dostupne_knihy()

    elif menu == "6":
        print("Koniec programu.")
        break

    else:
        print("Neplatná voľba, skús znova.")

