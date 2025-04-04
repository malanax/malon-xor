nr = input("Introduceti un numar: \n")

sum = 0
i = 0
while i < len(nr):
    sum += int(nr[i])
    i += 1

print(sum)
