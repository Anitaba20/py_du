# # DU z 4.11.25 Vypíše počet samohlások z textu ktorý zadá používateľ

t = input("Zadaj ľubovolný text: ")

samohlasky = "aeiouyAEIOUY"
pocet_samohlasok = 0

for i in samohlasky:
    pocet_samohlasok += t.count(i)
print("Počet samohlások z textu:", pocet_samohlasok)

for i in samohlasky:
    print(f"Samohláska '{i}': {t.count(i)}")