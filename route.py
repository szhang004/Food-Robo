import requests
api_url = "http://router.project-osrm.org/route/v1/foot/34.0212327,-118.2866796;34.0219843,-118.2893943?overview=false"
response = requests.get(api_url)
response = response.json()
print(response['message'])