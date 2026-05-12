class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):   #getter
        return self.__name

    def get_age(self):
        return self.__age


    def set_name(self, name):  #setter
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        print("Животное издает звук")

class Dog(Animal):
    def make_sound(self):
        print("Собака говорит: Гав-гав!")


class Cat(Animal):
    def make_sound(self):
        print("Кошка говорит: Мяу-мяу!")


dog = Dog("Барсик", 5)   # animals
kitty = Cat("Мурзик", 2)

dog.make_sound()   # Полиморфизм
kitty.make_sound()


print(dog.get_name())   #Getters
print(dog.get_age())

print(kitty.get_name())
print(kitty.get_age())

kitty.set_age(3)     #SETTERS
dog.set_name("Зюзя")

print(kitty.get_age())   # Проверка
print(dog.get_name())