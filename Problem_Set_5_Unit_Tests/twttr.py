def main():
    word = input("Input: ")
    print(shorten(word))




# def shorten(word):
#     output = ""
#     for letter in word:
#         if letter.lower() not in ['a', 'e', 'i', 'o', 'u']: 
#             output += letter
#     return f"Output: {output}"

# An Even Faster Pythonic Alternative is by usig List Comprehension

def shorten(word):
    output = "".join([letter for letter in word if letter.lower() not in "aeiou"])
    return f"Output: {output}"


if __name__ == "__main__":
    main()