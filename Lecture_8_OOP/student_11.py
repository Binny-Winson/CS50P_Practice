class Student:
    def __init__(self, name, house, patronus=None):
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} is in {self.house} and conjures up a {self.patronus}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Missing house")
        self._house = house

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russel Terrier":
                return "🐶"
            case _:
                return "🪄"
            
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ") or None
        return cls(name, house, patronus)

def main():
    student = Student.get()
    print(student, end=" ")
    print(student.charm())

main()
    