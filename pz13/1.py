'''
В двумерном списке найти среднее арифметическое положительных элементов, кратных 3. Матрица должна генерироваться рандомно. Используй lambda
'''
import random
cols = 3
rows = 3
matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
print(matrix)

def summ(matrix):
    mat = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            mat.append(matrix[i][j])

    ok = list(filter(lambda x: x > 0 and x % 3 == 0, mat))
    if not ok:
        return 0
    result = sum(ok) / len(ok)
    return result

print(summ(matrix))
