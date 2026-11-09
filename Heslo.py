pocitadlo =3
while pocitadlo <= 3 and pocitadlo > 0:
    heslo = input("Zadejte heslo: ")
    if heslo == "polyna":
        print("heslo je spravne")
        break
    else:
        print("heslo je spatne")
        pocitadlo -= 1
        if pocitadlo == 0:
            print("Vycerpali jste vsechny pokusy.")