"""
Дано целое число N (> 0). Найти сумму N^2 + (N + 1)^2 + (N + 2)^2 + ... + (2N)^2
"""

while True:
    try:
        n = int(input("введите целое число: "))
        if n > 0:
            summ = 0
            for i in range(n, 2 * n + 1):
                summ += (i ** 2)
                ts = summ + (2 * n) ** 2
            print(ts)
            break
        else:
            print("введите число больше 0")

    except ValueError:
        print("Введите число!!!")

