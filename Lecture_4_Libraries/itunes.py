import sys, requests, json  

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")
# print(json.dumps(response.json(), indent = 2))

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=weezer")

o = response.json()

for result in o['results']:
    print(result['trackName'])