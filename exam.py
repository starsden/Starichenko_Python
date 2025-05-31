a = list(input("Ваша карта: "))

def maskify(a):
    b = len(a) - 4
    for i in range(b):
        a[i] = '#'
    return ''.join(a)

print(maskify(a))