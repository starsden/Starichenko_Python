"""
Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
получится нуль?

"""
while True:
    try:
        num = int(input("Введите число: "))
        def main(a):
            steps = 0
            while a > 0:
                summ = 0
                temp = a
                while temp > 0:
                    summ += temp % 10
                    temp = temp // 10
                a = a - summ
                steps += 1
            return steps

        print(f"Количество операций:", main(num))
        break

    except ValueError:
        print('Введите число!!!')
