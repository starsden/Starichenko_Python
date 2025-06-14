'''
Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
"Человек". Каждый класс должен иметь метод, который выводит информацию о поле объекта.
'''

class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self) -> None:
        print(f"Имя: {self.name}\nВозраст: {self.age}\nПол: {self.gender}")


class Man(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender="Мужской")

    def gend(self) -> None:
        print(f"{self.name} — мужчина.")


class Woman(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender="Женский")

    def gend(self) -> None:
        print(f"{self.name} — женщина.")



ivan = Man("Иван", 30)
print(dir(ivan), "\n")
ivan.info()
ivan.gend()

maria = Woman("Мария", 25)
print(dir(maria), "\n")
maria.info()
maria.gend()
