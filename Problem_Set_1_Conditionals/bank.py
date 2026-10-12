prompt = input("Greeting: ").strip().lower()

# if "hello" in prompt:
#     print("$0")

if prompt.startswith("hello"):
    print("$0")
elif prompt[0] == "h":
    print("$20")
else:
    print("$100")