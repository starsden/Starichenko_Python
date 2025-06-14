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
    if 1 <= N < 4:
        norm = N - 1
        summ = sum(a[norm])
        p = 1
        res = 1
        for i in range(len(a[norm])):

            p = a[norm][i]
            res = (lambda x, y: x * y)(p, res)

        print(f"произведение: {res}")
        print(f'сумма: {summ}')
    else:
        return None

mult(matrix)