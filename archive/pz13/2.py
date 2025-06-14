'''
В двумерном списке элементы строки N (N задать с клавиатуры) увеличить на 3.
'''
import random

cols = 3
rows = 3
matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
print(matrix)

def summ(a):
    N = int(input("введите номер строки: "))
    if 0 <= N < 4:
        norm = N - 1
        a[norm] = list(map(lambda x: x + 3, a[norm]))
        for row in a:
            print(row)
        return a
    else:
        return None

summ(matrix)