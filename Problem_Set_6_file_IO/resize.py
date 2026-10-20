from PIL import Image

image_1, image_2 = Image.open("binny.png"), Image.open("shirt_1.png")
print(image_1.size)
print(image_2.size)
image_3 = image_2.resize((413,531))
print(image_3.size)
image_3.save("shirt.png", save_all = True)
