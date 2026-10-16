from pyfiglet import Figlet
import random
import sys


figlet = Figlet()

font_list = figlet.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    selected_font = random.choice(font_list)
    figlet.setFont(font=selected_font)
    print("Output:")
    print(figlet.renderText(text))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    text = input("Input: ")
    selected_font = sys.argv[2]
    if selected_font in font_list:
        figlet.setFont(font=selected_font)
    else:
        sys.exit("Invalid usage")
    print("Output:")
    print(figlet.renderText(text))

else:
    sys.exit("Invalid usage")