# Extracting text from user input using re.search
# Input: https://twitter.com/davidjmalan

import re

url = input("URL: ").strip()

# username = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# if username:
#     print(f"Username: {username.group(2)}")


# if username := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):

if username := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: {username.group(1)}")
