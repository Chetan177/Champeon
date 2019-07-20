
import pandas as pd
import json
import requests
from data_Per import *
from data_process import *

'''
This module handle the data gathering process from the API 

All the documentation regarding the API is available at:
https://documentation.pubg.com/en/index.html

'''

# Shard specification: url = "https://api.pubg.com/shards/[SHARD HERE]/" 
# Here we are only looking for steam useers

url = "https://api.pubg.com/shards/steam/" 

headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwOTI4NTQ0MC04YzRmLTAxMzctNDRiYy02Yjk0MzRkYzNmOGUiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTYzNTM5NDgwLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImNoZXRhbnBhbmRleTE3In0.cgjgrI1NLmvZHZmFFbDZsV9vGfxnD8vjqqnLEkMw4p0",
            "Accept": "application/vnd.api+json"}  # Dictionary which contains API key to access the API

final_data = pd.DataFrame()
def get_match_list(userid):
    # Generating the user url
    user_url = url + "players?filter[playerNames]=" + userid 

    req = requests.get(user_url, headers = headers)
    if req.status_code == 200:
	    print("Successfully Connected!!!")
    else:
        print("Failed to Connect!!!")
    player_stat = json.loads(req.text)

    match_id_list = player_stat['data'][0]['relationships']['matches']['data']  # Json list which contains all match ids
    return match_id_list


# Info of each match
def get_match_stats(match_stat):
  match_id = match_stat['data']['id']
  match_attributes = match_stat['data']['attributes']
  return match_id,match_attributes

# The performance stats of the searched player in each match
def get_performance(userid, match_stat):
  match_included = match_stat['included']
  for i in match_included:
    if (i['type'] == 'participant' and i['attributes']['stats']['name'] == userid):
      per_info = i['attributes']['stats']
      
  return per_info


  # Example match url format: "https://api.pubg.com/shards/steam/matches/{id}"
def get_performance_stat(userid):
    match_id_list = get_match_list(userid)
    P = data_per(userid)
    for match in match_id_list:
        match_id = match['id']
        match_url = url + "matches/{}".format(match_id)
        match_r = requests.get(match_url, headers = headers)
        if match_r.status_code != 200:
            print("Failed to Connect!!!")
        


        match_stat = json.loads(match_r.text)
        match_data =get_match_stats(match_stat)
        per_data= get_performance(userid, match_stat)
        
        
        P.set_perf_info(per_data)
        P.set_match_stat(match_data[0],match_data[1])
    
    return P.return_data()
  


#x=get_performance_stat("SIKHWARRIOR")
#print(len(x))
def get_data_to_predict(userid):
    data = get_performance_stat(userid)
    data = list(data)
    final_data = generate_data(data)
    return final_data





