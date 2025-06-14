'''
В двумерном списке найти сумму и произведение элементов строки N (N задать с клавиатуры).
'''

import random

cols = 3
rows = 3
matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
print(matrix)
def mult(a):
    N = int(input("введите номер строки: "))
    if 0 <= N < 4:
        norm = N - 1
        p = 1
        for i in range(len(matrix[norm])):
            p *= matrix[norm][i]
        print(f"произведение: {p}")
    else:
        return None

mult(matrix)