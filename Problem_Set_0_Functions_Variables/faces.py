def convert(speech):
    new_speech = speech.replace(":)", "🙂").replace(":(", "🙁")
    print(new_speech)

def main():
    speech = input("What do you want to say? ")
    convert(speech)

main()