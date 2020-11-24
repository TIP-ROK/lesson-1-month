class Human:
    def __init__(self, name, surname, age, weight):
        self.name =name
        self.surname = surname
        self.age = age
        self.weight = weight

    def __str__(self):
        print(f"{self.name} {self.surname} {self.age} {self.weight}")

    def live(self):
        return "Ok"
    def get_name(self):
        return self.name

class Citizen(Human):
    def __init__(self, name, surname, age, weight):
        super(Citizen,self).__init__(name, surname, age, weight, country)
        self.country = country

class Student(Citizen):

    def __init__(self, name, surname, age, weight, university, faculty, course):
        super(Student,self).__init__(name, surname, age, weight, country)
        self.university = university
        self.faculty = faculty
        self.course = course