'''
В двумерном списке найти среднее арифметическое положительных элементов, кратных 3.
'''

matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]
total = 0
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 0 and matrix[i][j] % 3 == 0:
            total += matrix[i][j]
            count += 1
print(total / count)