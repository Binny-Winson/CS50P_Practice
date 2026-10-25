class Student:
    def __init__(self, name, house, patronus = None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            raise ValueError("Invalid patronus")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house} and {self.patronus}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🫎"
            case "Otter":
                return "🦦"
            case "Jack Russell Terrier":
                return "🐶"
            case _:
                return "🪄"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()