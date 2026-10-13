variable_name = input("camelCase: ").strip()
snake_case = ""
for char in variable_name:
    # if char == char.upper(): --> the safer option is to use .isupper() method
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char

print(f"snake_case: {snake_case}")
