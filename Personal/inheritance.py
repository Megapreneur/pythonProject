class Animal:
    def __init__(self, name):
        self.name = name

    def  speak(self):
        return "i speak"


class Dog(Animal):
    def __init__(self, name, type_):
        super().__init__(name)
        self.type = type_


class Cat(Animal):
    pass


dog = Dog("Bingo")
cat = Cat("Puss")

print(dog.name)
print(dog.speak())
