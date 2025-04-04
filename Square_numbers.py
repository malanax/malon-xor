'''
Exercițiul 2: Numere pare**
Cerinta: Parcurge lista de numere și afișează doar numerele pare.
Input: `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]`
Output:
```
Număr par: 2
Număr par: 4
Număr par: 6
Număr par: 8
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number % 2 == 0:
        print(number)