import validator_collection

email = input("What's your email address? ").strip()

try:
    validated_email = validator_collection.email(email)
    if validated_email:
        print("Valid")
except validator_collection.errors.InvalidEmailError:
    print("Invalid")

