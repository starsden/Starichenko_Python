'''
Из предложенного текстового файла (text18-27.txt) вывести на экран его содержимое,
количество пробельных символов. Сформировать новый файл, в который поместить текст
в стихотворной форме предварительно поставив последнюю строку фразой введенной
пользователем.
'''

file = open('text18-27.txt', 'r', encoding='utf-16')
content = file.read()
file.close()

print(content)
print('\n\nкол-во пробелов:', content.count(' '))

a = input('введи фразу: ')
fule = open('result2.txt', 'w', encoding='utf-16')
fule.write(content + '\n' + a)
