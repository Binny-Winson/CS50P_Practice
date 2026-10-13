vovels = ['a', 'e', 'i', 'o', 'u']

text_with_vovels_omitted = ""

original_text = input("Input: ")

for letter in original_text:
    if letter not in vovels:
        text_with_vovels_omitted += letter

print(f"Output: {text_with_vovels_omitted}")