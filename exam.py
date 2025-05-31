try:
    file = open('exmple.txt', 'r')
    a = file.read()
    file.close()

    for strok in a.split('\n'):
        print(strok)

except FileNotFoundError:
    print("Файла нет")
