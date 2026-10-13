# while True:
#     x = int(input("What's x: "))
#     if x < 0:
#         continue
#     else:
#         break

# for _ in range(x):
#     print("meow")

# the continue keyword is redundant in this case. We can improve our code as follows:

while True:
    x = int(input("What's x? "))
    if x > 0:
        break

for _ in range(x):
    print("meow")