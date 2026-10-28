class Package:
    def __inti__(self, id, sender, recepient, weight):
        self.id = id
        self.sender = sender
        self.recepient = recepient
        self.weight = weight

def main():
    packages = [
        Package(id = 1, sender = "Alice", recepient = "Bob", weight = 10),
        Package(id = 2, sender = "Bob", recepient = "Charlie", weight = 5)
    ]
    print(packages)
main()