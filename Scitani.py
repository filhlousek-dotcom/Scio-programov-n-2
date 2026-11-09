cislo = 1
vysledek = 0
while cislo >0:
    cislo = (int(input("Zadej číslo: ")))
    print(f"Zadal jsi {cislo}")
    vysledek += cislo
    print(f"Součet je {vysledek}")
if cislo <= 0:
    print("Zadal jsi neplatné číslo.")
    