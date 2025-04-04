numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    se_imparte = 0
    for i in range(2,number):
        if number % i == 0:
            se_imparte = 1

    if se_imparte == 0:
        print(f"Numar prim: {number}")




