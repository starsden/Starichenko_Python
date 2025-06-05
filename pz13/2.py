'''
В двумерном списке элементы строки N (N задать с клавиатуры) увеличить на 3.
'''


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


N = int(input("введите номер строки "))
if 0 <= N < len(matrix):
    matrix[N] = [x + 3 for x in matrix[N]]
    print("Изменённая матрица:")
    for row in matrix:
        print(row)
else:
    print("Некорректный номер строки.")