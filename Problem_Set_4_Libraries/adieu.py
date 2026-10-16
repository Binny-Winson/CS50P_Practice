# p.join(('apples', 'bananas', 'carrots'), conj='and even')
# ans ---> 'apples, bananas, and even carrots'

import inflect

p = inflect.engine()

names_list = []

while True:
    try:
        name = input("Name: ").title()
        names_list.append(name)
        continue
    except (EOFError, ValueError):
        break

print(f"Adieu, adieu, to {p.join(names_list, conj = 'and')}")