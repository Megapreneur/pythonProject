class Person:
    ID = 0

    def _int_(self, first_name, last_name, year, month, day):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.year = year
        self.month = month
        self.day = day
        Person.ID += 1

    def repr(self):
        return f"<Person: {self.first_name}"

    def str(self):
        return f"<Person: {{name={self.first_name}, {self.last_name}, age={self.age}}}"

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, year):
        if age < 18:
            raise ValueError("This website is info is strictly for 18+")
        self.age = 2022 - year

    @property
    def age(self):
        return self.age

    @age.deleter
    def age(self):
        print("Age deleted")
        del self.age

    @classmethod
    def get_nun_of_id(cls):
        return cls.ID

    @staticmethod
    def get_age(age):
        return age


p1 = Person("akin", "tayo", 1990, "april", 22)
print(Person.ID)