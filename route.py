import requests
import json

api_url = "http://router.project-osrm.org/route/v1/foot/-118.283752,34.0215692;-118.2900851,34.0196828?overview=false&alternatives=true&steps=true"
response = requests.get(api_url)
response = response.json()

i = 0 

while (1):
    try:
        print(response["routes"][0]['legs'][0]['steps'][0]['intersections'][i]['location'])
        i += 1
    except: 
        break