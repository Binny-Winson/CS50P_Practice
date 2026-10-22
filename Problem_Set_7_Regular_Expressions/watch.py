import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'src=["\']?(https?://)?(?:www\.)?youtube\.com/embed/([^"\'\?&$\s>/]{11})(?:[^"\'>]*["\'>\s]|$)', s):
        protocol = match.group(1) if match.group(1) else "https://"
        return protocol + "youtu.be/" + match.group(2)
    return None


if __name__ == "__main__":
    main()