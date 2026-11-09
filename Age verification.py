vek = float(input("Zadej svůj věk: ") )
if vek >= 18:
    print("Muzes hrat")
else:
    rozdil = 18 - vek
    print (f"Tohle není pro tebe, vrat se za {rozdil} let.")
