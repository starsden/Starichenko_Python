"""
В последовательности их N чисел (N -четное) в первой ее половине найти
произведение элементов меньших 0.
"""
from functools import reduce

n = int(input('введите четное число '))
a = list(map(int, input('введите числа ').split()))
b = []
for i in a:
    if i < 0:
        b.append(i)
print(b)
print(reduce(lambda x, y: x * y, b))