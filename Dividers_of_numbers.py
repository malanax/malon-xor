numere = []

for i in range(10):
    numere.append(int(input("Introduceti un numar: \n")))

divizor = int(input("Introduceti divizorul dorit: \n"))

for numar in numere:
    if numar % divizor == 0:
        print(f"Numar divizibil cu {divizor}: {numar}")
