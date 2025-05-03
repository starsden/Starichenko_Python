with open("file1.txt", "w") as f1:
    f1.write("1 -2 3 -4 5")

with open("file2.txt", "w") as f2:
    f2.write("-4 5 -6 7")

a = list(map(int, open("file1.txt").read().split()))
b = list(map(int, open("file2.txt").read().split()))

a_in_b = [str(x) for x in a if x in b]
b_in_a = [str(x) for x in b if x in a]

all_numbers = a + b

total = len(all_numbers)
positive = len([x for x in all_numbers if x > 0])
negative = len([x for x in all_numbers if x < 0])

with open("result.txt", "w") as res:
    res.write("Элементы первого и второго файлов:\n")
    res.write(" ".join(map(str, a)) + "\n")
    res.write(" ".join(map(str, b)) + "\n\n")
    res.write("Элементы первого файла, присутствующие во втором:\n")
    res.write(" ".join(a_in_b) + "\n\n")
    res.write("Элементы второго файла, присутствующие в первом:\n")
    res.write(" ".join(b_in_a) + "\n\n")
    res.write(f"Количество элементов: {total}\n")
    res.write(f"Количество отрицательных элементов: {negative}\n")
    res.write(f"Количество положительных элементов: {positive}\n")
ч