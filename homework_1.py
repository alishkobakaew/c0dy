class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        if self.higher_education:
            education = "есть высшее образование"
        else:
            education = "высшего образования нет"

        print("Меня зовут", self.name)
        print("Дата рождения:", self.birth_date)
        print("Профессия:", self.occupation)
        print(education)
        print()


# Создаем Информацию
person1 = Person("Алихан", "12.04.2005", "Повар", False)
person2 = Person("Айсулуу", "07.03.1992", "Бухгалтер", True)

# Вывод данных
print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print()

# Вывод информации
person1.introduce()
person2.introduce()