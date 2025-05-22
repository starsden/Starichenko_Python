"""
В последовательности их N чисел (N -четное) в первой ее половине найти
произведение элементов меньших 0.
"""

from functools import reduce
def product_negative_first_half(seq):
    half = seq[:len(seq) // 2]
    negatives = list(filter(lambda x: x < 0, half))
    return reduce(lambda a, b: a * b, negatives, 1)


def product_negative_first_half_lc(seq):
    negatives = [x for x in seq[:len(seq) // 2] if x < 0]
    return reduce(lambda a, b: a * b, negatives, 1)

if __name__ == "__main__":
    N = int(input("Введите четное число N: "))
    seq = list(map(int, input("Введите {} чисел через пробел: ".format(N)).split()))
    result = product_negative_first_half(seq)
    print("Произведение отрицательных элементов в первой половине:", result)