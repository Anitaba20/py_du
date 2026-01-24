# DU_2.12.2025_Operácie so zoznamami
# zadanie:
# Operácie so zoznamami
# Cieľ: Cieľom tejto úlohy je poskytnúť študentom praktické skúsenosti s manipuláciou
# so zoznamami v programovacom jazyku. Študenti sa naučia kombinovať zoznamy, sortovať
# dáta a vykonávať základné vyhľadávanie.

zoznam1 = [1, 11, 9, 3, 5]
zoznam2 = [20, 0, 4, 18, 2]
zoznam3 = [25, 30, 32, 6, 10]
zoznam4 = [24, 35, 12, 27, 16]

zoznamy_spolu = []
zoznamy_spolu.extend(zoznam1)
zoznamy_spolu.extend(zoznam2)
zoznamy_spolu.extend(zoznam3)
zoznamy_spolu.extend(zoznam4)

def sortuj(zoznam_cisel, vzostupne):
    return sorted(zoznam_cisel, reverse=not vzostupne)

def hladaj(zoznam_cisel, hladane_cislo):
    return hladane_cislo in zoznam_cisel

print(sortuj(zoznamy_spolu, True))
print(hladaj(zoznamy_spolu, 1))

