class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет, моя профессия — {self.profession}.")


class Classmate(Person):
    def __init__(self, name, age, profession, group_name):
        super().__init__(name, age, profession)
        self.group_name = group_name

    def introduce(self):
        print(
            f"Привет! Я {self.name}, мне {self.age} лет. "
            f"Я учусь в группе {self.group_name} и моя профессия — {self.profession}."
        )


class Friend(Person):
    def __init__(self, name, age, profession, hobby):
        super().__init__(name, age, profession)
        self.hobby = hobby

    def introduce(self):
        print(
            f"Привет! Меня зовут {self.name}, мне {self.age} лет. "
            f"Я работаю как {self.profession}, а мое хобби — {self.hobby}."
        )


# Classmate
classmate1 = Classmate("Азамат", 19, "студент", "ИБ-2")
classmate2 = Classmate("Алия", 20, "студент", "ИБ-3")

# FRIEND
friend1 = Friend("Турат", 21, "дизайнер", "бильярд")
friend2 = Friend("Айсулуу", 22, "программист", "пение")

# Вызов метода introduce()
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()
