import os
import sys

from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

ext1 = os.path.splitext(sys.argv[1])[1].lower()
ext2 = os.path.splitext(sys.argv[2])[1].lower()

valid_extensions = ['.jpg', '.jpeg', '.png']

if ext1 not in valid_extensions or ext2 not in valid_extensions:
    sys.exit("Invalid output")

if ext1 != ext2:
    sys.exit("Input and output have different extensions")

if not os.path.isfile(sys.argv[1]):
    sys.exit("Input does not exist")

try:
    with Image.open(sys.argv[1]) as photo, Image.open("shirt.png") as shirt:
        photo = ImageOps.fit(photo, size=shirt)
        photo.paste(shirt, (0,0), shirt)
        photo.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input file does not exist")
