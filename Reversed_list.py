'''
**Exercițiul 3: Afișarea numerelor invers**
Cerinta: Parcurge lista de numere și afișează-le în ordine inversă.
Input: `numbers = [10, 20, 30, 40, 50]`
Output:
```
Număr invers: 50
Număr invers: 40
Număr invers: 30
Număr invers: 20
Număr invers: 10
```
'''

numbers = [10, 20, 30, 40, 50]

for i in reversed(numbers[::]):
    print(i)
