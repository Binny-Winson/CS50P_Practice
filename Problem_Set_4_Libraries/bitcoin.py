import requests, sys

if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=95aee8e6f12cae3ed71294e057fa2cadf71624e141f9124611d413feb1e710cc")
except requests.RequestException:
     sys.exit()

price = n * float(response.json()["data"]["priceUsd"])
print(f"${price:,.4f}")
