# Inheritance

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

    def __str__(self):
        return f"{self.name} is a wizard"

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"{super().__str__()} is in {self.house}"

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"{super().__str__()} teaches {self.subject}"

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
profesor = Professor("Severus", "Defense against the dark arts")

print(wizard)
print(student)
print(profesor)