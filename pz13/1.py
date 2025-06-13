'''
В двумерном списке найти среднее арифметическое положительных элементов, кратных 3. Матрица должна генерироваться рандомно
'''
import random
cols = 3
rows = 3
matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
print(matrix)

def summ(matrix):
    total = 0
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0 and matrix[i][j] % 3 == 0:
                total += matrix[i][j]
                count += 1

    result = total / count
    return result

print(summ(matrix))