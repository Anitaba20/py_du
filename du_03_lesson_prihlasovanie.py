# # Du zo dňa 28.10.2025

spravne_meno = "Používateľ"
spravne_heslo = 12345
try:
    zadane_meno = input("Zadaj svoje meno: ")
    zadane_heslo = int(input("Zadaj heslo: "))

    if zadane_meno == spravne_meno and zadane_heslo == spravne_heslo:
        print("Prihlásenie úspešné!")
    else:
        print("Nesprávne meno alebo heslo!")

except ValueError:
    print("Heslo musí byť číslo!")