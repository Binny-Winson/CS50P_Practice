import os
import sys

from PIL import Image, ImageOps

# Check if the user provided too many command-line arguments (more than 2 file paths)
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Check if the user provided too few command-line arguments (fewer than 2 file paths)
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

# Extract the file extensions from the input and output arguments and convert them to lowercase
ext1 = os.path.splitext(sys.argv[1])[1].lower()
ext2 = os.path.splitext(sys.argv[2])[1].lower()
# Define the list of allowed image extensions for this program
valid_extensions = [".jpg", ".jpeg", ".png"]

# Verify that both the input and output file extensions are valid formats
if ext1 not in valid_extensions or ext2 not in valid_extensions:
    sys.exit("Invalid input")
# Ensure that the input file extension matches the output file extension exactly
if ext1 != ext2:
    sys.exit("Input and output have different extensions")

# Check the local filesystem to confirm that the input file actually exists
if not os.path.isfile(sys.argv[1]):
    sys.exit("Invalid input")

try:
    # Attempt to open the background image (input) and the overlay shirt image template
    with Image.open(sys.argv[1]) as image_1, Image.open("shirt.png") as image_2:
        # Determine the width and height dimensions of the overlay shirt image
        shirt_size = image_2.size
        # Crop and resize the input image so it fits the shirt dimensions perfectly
        image_1 = ImageOps.fit(image_1, shirt_size)
        # Overlay the shirt onto the input image, using the shirt as its own transparency mask
        image_1.paste(image_2, (0, 0), image_2)
        # Save the finalized image composite to the requested output path
        image_1.save(sys.argv[2])
except FileNotFoundError:
    # Handle the error gracefully if one of the image assets fails to load from disk
    sys.exit("Input file does not exist")