# # du z 11.11.25_Vypíš tabuľku násobilky pre čísla 1–10 pomocou vnorených cyklov.
for r in range(1, 11):
    for s in range(1, 11):
        print(r * s, end="|")
    print()