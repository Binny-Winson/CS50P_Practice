name = input("What's your name? ").strip()

if "," in name:
    last_name, first_name = name.split(", ")
    name = f"{first_name} {last_name}"
print(f"Hello, {name}")