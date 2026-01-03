# # du z 18.11.25_teplotný konvertor
def konvertuj_teplotu(teplota, jednotka):
    if jednotka == "C":
        return teplota * 9/5 + 32
    elif jednotka == "F":
        return (teplota - 32) * 5/9
    else:
        print("Neplatná jednotka! Použite 'C' alebo 'F' ")

print(konvertuj_teplotu(100, "C"))

print(konvertuj_teplotu(32, "F"))