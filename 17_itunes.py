# Day 4: Dec 15, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 

import json
import requests
import sys

if len(sys.argv) != 2:
        sys.exit()

# use the requests library to connect to the web APIs
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=bruno+mars" 
             + sys.argv[1])

# use json.dumps to make the json data easier to read
# this will print all json data from the requests
print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
        print(result["trackName"])