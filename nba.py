import requests
import json

url = "https://api.balldontlie.io/v1/players"
headers = {
  # don't know how to use it from .gitignore rather than writing it here
  "Authorization": "17e7db08-b11f-4589-9397-21ba5ed3feda" 
}
params = {"search": "curry"}
params2 = {"player_ids[]": 228} #Kyrie
params_stats = {"player_ids[]": 228, "seasons[]": "2024"}
try:
  #response = requests.get(url, params=params2, headers=headers)
  # cannot print out stats at all for some reason
  #response = requests.get("https://api.balldontlie.io/v1/stats?seasons[]=2022&player_ids[]=228", headers=headers)
  #response = requests.get(url, params=params_stats, headers=headers)
  response = requests.get(url, params=params, headers=headers)
  response.raise_for_status()
  json_data = json.loads(response.text)
  for player in json_data['data']:
    # all of people with last name 'curry', get stephen curry and his team
    if player['first_name'] == 'Stephen':
      print(f"{player['first_name']} {player['last_name']} plays for the {player['team']['full_name']}")

except requests.exceptions.RequestException as e:
    print("Error:", e) 


#curl "https://api.balldontlie.io/v1/players" -H "Authorization: 17e7db08-b11f-4589-9397-21ba5ed3feda"
#curl "https://api.balldontlie.io/v1/players?search=curry" -H "Authorization: 17e7db08-b11f-4589-9397-21ba5ed3feda"