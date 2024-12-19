"""
Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти
наименьший периметр треугольника, вершины которого принадлежат различным
точкам множества A, и сами эти точки (точки выводятся в том же порядке, в котором
они перечислены при задании множества A).
Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
R = √(x2 – x1)2 + (у2 – y1)2
.
Для хранения данных о каждом наборе точек следует использовать по два списка: первый
список для хранения абсцисс, второй — для хранения ординат.

"""
from itertools import combinations
import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def min(x, y):
    n = len(x)
    if n < 3:
        return "минимум 3 точки"

    min_perimeter = float('inf')
    triang = ()

    for i, j, k in combinations(range(n), 3):

        x1, y1 = x[i], y[i]
        x2, y2 = x[j], y[j]
        x3, y3 = x[k], y[k]

        a = dist(x1, y1, x2, y2)
        b = dist(x2, y2, x3, y3)
        c = dist(x3, y3, x1, y1)

        perimeter = a + b + c

        if perimeter < min_perimeter:
            min_perimeter = perimeter
            triang = ((x1, y1), (x2, y2), (x3, y3))

    return min_perimeter, triang


x = [0, 0, 1, 2, 3]
y = [0, 2, 1, 1, 0]

result = min(x, y)
print("Минимальный периметр:", result[0])
print("Точки треугольника:", result[1])