# du z 16.12.25_nahradenie slov v texte zo suboru
with open("vstup.txt", "r") as first_file:
    slovo = first_file.read()

zmena_slova = slovo.replace("pes", "kôň")

with open("vystup.txt", "x") as second_file:
    second_file.write(zmena_slova)


# bez automatickeho ukladania_namiesto rezimu x - rezim w
first_file = open("vstup.txt", "r")
slovo = first_file.read()
first_file.close()

zmena_slova = slovo.replace("pes", "kôň")

second_file = open("vystup.txt", "w")
second_file.write(zmena_slova)
second_file.close()