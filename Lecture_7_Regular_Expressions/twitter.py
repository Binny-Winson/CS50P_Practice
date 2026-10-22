import re

url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# username = re.sub(r"^(https?://)?(www\.)?([^/]+\.([^/]+)/)", "", url)

username = re.sub(r"^(https?://)?(www\.)?.+\..+/", "", url)

print(username)