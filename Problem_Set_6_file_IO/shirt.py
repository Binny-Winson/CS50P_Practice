import os
import sys

from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

ext1 = os.path.splitext(sys.argv[1])[1].lower()
ext2 = os.path.splitext(sys.argv[2])[1].lower()
valid_extensions = [".jpg", ".jpeg", ".png"]

if ext1 not in valid_extensions or ext2 not in valid_extensions:
    sys.exit("Invalid input")
if ext1 != ext2:
    sys.exit("Input and output have different extensions")

if not os.path.isfile(sys.argv[1]):
    sys.exit("Invalid input")

try:
    with Image.open(sys.argv[1]) as image_1, Image.open("shirt.png") as image_2:
        shirt_size = image_2.size
        image_1 = ImageOps.fit(image_1, shirt_size)
        image_1.paste(image_2, (0, 0), image_2)
        image_1.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input file does not exist")