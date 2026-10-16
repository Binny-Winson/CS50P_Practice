import random

def main():
    level = get_level()
    score = 0
    questions = 0
    
    while questions < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        
        attempt = 0
        while attempt < 3:
            answer = input(f"{x} + {y} = ")
            if not answer.isdigit() or int(answer) != x + y:
                print("EEE")
                attempt += 1
            elif int(answer) == x + y:
                score += 1
                break
        if attempt == 3:
            print(f"{x} + {y} = {x + y}")
        
        questions += 1            
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()