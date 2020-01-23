# Implement Students room using OOP:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

class Students_room:
    """ Данные о студенте """
    def __init__(self, name, surname, age, specialty):
        self.name = name
        self.surname = surname
        self.age = age
        self.specialty = specialty

    """ Вывод информации о студенте """
    def __repr__(self):
        print(f"name: {self.name.title()} {self.surname.title()}, "
              f"age: {self.age}, specialty: {self.specialty.title()}")
        return(f"name: {self.name.title()} {self.surname.title()}, "
              f"age: {self.age}, specialty: {self.specialty.title()}")

Steve = Students_room("Steven", "Schultz", 23, "English")
Johnny = Students_room("Jonathan", "Rosenberg", 24, "Biology")
print(Steve)
print(Johnny)
Steve.__repr__()