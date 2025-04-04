numbers = [1, 2, 3, 4, 5]

for index in range(len(numbers)-1):
    print(numbers[index] + numbers[index+1])
    if numbers[index+1] == numbers[-1]:
        break


