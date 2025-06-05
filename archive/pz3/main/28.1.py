'''
Даны числа x, у. Проверить истинность высказывания: «Точка с координатами (x, у)
лежит в первой или третьей координатной четверти».
'''

while True:
    try:
        x = float(input("x: "))
        y = float(input("y: "))

        if (x > 0 and y > 0) or (x < 0 and y < 0):
            print('true')
        else:
            print('false')
        break
    except ValueError:
        print("Неверное значение")
