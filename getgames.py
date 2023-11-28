#!/usr/bin/env python
""" Download games from a chess.com user

    Usage: python getgames.py <username>
"""

from urllib.request import urlopen
import os
import json
import sys

username = str(sys.argv[1])
url = "https://api.chess.com/pub/player/" + username + "/games/archives"
response = urlopen(url)
data_json = json.load(response)

all_games = []
longest_streak = 0
current_streak = 0
for month_url in data_json['archives']:
  month_games = json.load(urlopen(month_url))['games']
  print( "Loading games form " + month_url )
  for game in month_games:
    all_games.append(game)
  print("Retrived " + str(len(all_games)) + " games...")

#Make the games directory, so that we can store the files in it
os.makedirs("games/", exist_ok = True)

filename = "games/" + username + ".json"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(all_games, f, ensure_ascii=False, indent=2)
