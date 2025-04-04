numbers = [10, 20, 30, -5, 40, 50]

sum = 0
for number in numbers:
    if number >= 0:
        sum += number
    else:
        break

print(f"Suma este: {sum}")