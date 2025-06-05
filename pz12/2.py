"""
Составить генератор (yield), который переведет символы строки из нижнего
регистра в верхний.
"""
def gen(s):
    for char in s:
        yield char.upper()

text = input('введите строку: ')

res = gen(text)
result = ''.join(res)
print(result)