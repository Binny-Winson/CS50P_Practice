import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

randnum = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        if guess < randnum:
            print("Too small!")
        elif guess > randnum:
            print("Too Large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
        