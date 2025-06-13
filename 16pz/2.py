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

    def print_gender(self) -> None:
        print(f"{self.name} — мужчина.")


class Woman(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender="Женский")

    def print_gender(self) -> None:
        print(f"{self.name} — женщина.")



if __name__ == "__main__":
    ivan = Man("Иван", 30)
    maria = Woman("Мария", 25)

    ivan.info()
    ivan.print_gender()

    print("---")

    maria.info()
    maria.print_gender()
