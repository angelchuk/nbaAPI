import requests
import json
import pandas as pd
import sqlalchemy as db

url = "https://api.balldontlie.io/v1/players"
headers = {
  # don't know how to use it from .gitignore rather than writing it here
  "Authorization": "17e7db08-b11f-4589-9397-21ba5ed3feda" 
}
params = {"search": "curry"}
#params2 = {"player_ids[]": 228} #Kyrie
#params_stats = {"player_ids[]": 228, "seasons[]": "2024"}

  #response = requests.get(url, params=params2, headers=headers)
  # cannot print out stats at all for some reason
  #response = requests.get("https://api.balldontlie.io/v1/stats?seasons[]=2022&player_ids[]=228", headers=headers)
  #response = requests.get(url, params=params_stats, headers=headers)
response = requests.get(url, params=params, headers=headers)
response.raise_for_status()
curry_info = response.json()
  
print(json.dumps(curry_info, indent=4))

# extract 'data' field from json
players_data = curry_info['data']

# flatten nested dictionaries in the data for all "curry"s
flattened_data = []
for player in players_data:
    flattened_player = {}
    for key, value in player.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                flattened_player[f"{key}_{sub_key}"] = sub_value
        else:
            flattened_player[key] = value
    flattened_data.append(flattened_player)

dataf = pd.DataFrame(flattened_data)
  #json_data = json.loads(response.text)
engine = db.create_engine('sqlite:///nba_db.db')
dataf.to_sql('curry_table', con=engine, if_exists='replace', index=False)
with engine.connect() as connection:
  query_result = connection.execute(db.text("SELECT * FROM curry_table;")).fetchall()
  print(pd.DataFrame(query_result))
  #for player in json_data['data']:
    # all of people with last name 'curry', get stephen curry and his team
    #if player['first_name'] == 'Stephen':
      #print(f"{player['first_name']} {player['last_name']} plays for the {player['team']['full_name']}")



#curl "https://api.balldontlie.io/v1/players" -H "Authorization: 17e7db08-b11f-4589-9397-21ba5ed3feda"
#curl "https://api.balldontlie.io/v1/players?search=curry" -H "Authorization: 17e7db08-b11f-4589-9397-21ba5ed3feda"