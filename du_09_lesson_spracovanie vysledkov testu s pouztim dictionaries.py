# du z 9.12.25_spracovanie vysledkov testu s pouztim dictionaries
studenti = {
    "Helena": 1,
    "Katka":  2,
    "Michal": 3
}

def pridat_studenta():
    meno = input("Zadaj meno študenta: ")
    if meno in studenti:
        print("Rovnaké meno študenta")
        return
    try:
        znamka = int(input("Zadaj známku: "))
        studenti[meno] = znamka
        print("Študent bol pridaný")
    except ValueError:
        print("Známka musí byť číslo")


def vymazat_studenta():
    meno = input("Vymazať študenta: ")
    if meno in studenti:
        del studenti[meno]
        print("Študent bol vymazaný")
    else:
        print("Študent nie je v zozname")

def aktualizovat_znamku():
    meno = input("Aktualizovať známku študenta: ")
    if meno in studenti:
        try:
            nova_znamka = int(input("Nová známka: "))
            studenti[meno] = nova_znamka
            print("Známka bola aktualizovaná")
        except ValueError:
            print("Známka musí byť číslo")
    else:
        print("Študent nie je v zozname")

def zobrazit_znamku():
    meno = input("Zadaj meno študenta: ")
    if meno in studenti:
        print("Známka:", studenti[meno])
    else:
        print("Študent neexistuje")

def spocitat_priemer():
    if studenti:
        sucet = sum(studenti.values())
        priemer = sucet / len(studenti)
        print("Priemerná známka všetkých študentov: ", priemer)

while True:
    print("\nNavigácia podľa čísla:")
    print("1 Pridať študenta so známkou")
    print("2 Vymazať študenta")
    print("3 Aktualizovať známku")
    print("4 Zobraziť známku študenta")
    print("5 Spočítať priemer známok všetkých študentov ")
    print("6 Ukončiť program")

    menu = input("Vyber číslo: ")

    if menu == "1":
        pridat_studenta()
    elif menu == "2":
        vymazat_studenta()
    elif menu == "3":
        aktualizovat_znamku()
    elif menu == "4":
        zobrazit_znamku()
    elif menu == "5":
        spocitat_priemer()
    elif menu == "6":
        print("Koniec")
        break