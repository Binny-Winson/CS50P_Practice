class Vault:
    def __init__(self, Galleons, Sickles, Knuts):
        self.Galleons = Galleons
        self.Sickles = Sickles
        self.Knuts = Knuts

    def __str__(self):
        return f"{self.Galleons} Galleons, {self.Sickles} Sickles, {self.Knuts} Knuts"

    def __add__(self, other):
        Galleons = self.Galleons + other.Galleons
        Sickles = self.Sickles + other.Sickles
        Knuts = self.Knuts + other.Knuts
        return Vault(Galleons, Sickles, Knuts)

harry = Vault(100, 50, 25)

weasley = Vault(25, 50, 100)

total = harry + weasley

print(harry)
print(weasley)
print(total)