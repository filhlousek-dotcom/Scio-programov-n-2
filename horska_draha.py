vyska = (float(input("Zadej svou výšku v centimetrech: ")))
if vyska >= 140:
    print("Vstup povolen, užij si jízdu")
else:
    rozdil = 140 - vyska
    print (f"Vstup zakázán do limitu ti chybí ještě {rozdil} centimetrů.")
