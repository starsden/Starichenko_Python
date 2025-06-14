'''Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
Добавьте методы для вычисления среднего балла и определения, является ли студент
отличником.
'''

class Student:
    name: str
    surname: str
    marks: list

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def avg(self):
        return sum(self.marks) / len(self.marks)

    def fiver(self):
        return sum(self.marks) / len(self.marks) >= 4.5

examp = Student("Денис", "Стариченко", [5, 5, 5, 5])
print(examp.avg())
print(examp.fiver())



