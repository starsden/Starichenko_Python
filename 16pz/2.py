'''
Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
"Человек". Каждый класс должен иметь метод, который выводит информацию о поле объекта.
'''

class person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self) -> None:
        print(f"Имя: {self.name}\nВозраст: {self.age}\nПол: {self.gender}")


class man(person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender="Мужской")

    def gend(self) -> None:
        print(f"{self.name} — мужчина.")


class woman(person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender="Женский")

    def gend(self) -> None:
        print(f"{self.name} — женщина.")



ivan = man("Иван", 30)
print(dir(ivan), "\n")
ivan.info()
ivan.gend()

maria = woman("Мария", 25)
print(dir(maria), "\n")
maria.info()
maria.gend()
