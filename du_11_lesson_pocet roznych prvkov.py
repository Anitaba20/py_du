# du_23.12.25_Počet rôznych prvkov
# Ak je daný zoznam čísel so všetkými jeho prvkami zoradenými vzostupne,
# určte a vypíšte počet rôznych
# prvkov v ňom.

cisla = input("Zadaj čísla: ").split()

posledne_cislo = cisla[0]
pocet_cisel = 1

for cislo in cisla:
    if cislo == posledne_cislo:
        pocet_cisel = pocet_cisel
    else:
        pocet_cisel = pocet_cisel + 1
        posledne_cislo = cislo

print(pocet_cisel)


# zadanie2_snakify_Dĺžka úsečky

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

a = float(input())
b = float(input())
c = float(input())
d = float(input())

print(distance(a, b, c, d))