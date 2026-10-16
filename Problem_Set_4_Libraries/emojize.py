import emoji

user_input = input("Input: ").strip().lower()

if "_" in user_input:
    print(emoji.emojize(f"{user_input}", language="alias"))
else:
    print(emoji.emojize(f"{user_input}", language="alias"))

