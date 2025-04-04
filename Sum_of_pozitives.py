suma = 0
param = True
while param:
    nr = int(input("Introduceti un numar pentru a fi adaugat in lista: \n"))

    if nr >= 0:
        suma += nr
    optiune = input("Doriti sa continuati? y/n\n")

    if optiune == "y":
        continue
    elif optiune == "n":
        print("Multumim ca ati folosit programul nostru!")
        print(f"Suma numerelor pozitive din lista introdusa de dumneavoastra este {suma}.")
        param = False
    else:
        print("Programul va continua; Introduceti doar 'y' sau 'n'")

