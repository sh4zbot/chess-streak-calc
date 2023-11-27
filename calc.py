#!/usr/bin/env python
""" Find a chess.com user's longest streak with links to all the games
    Print some stats.
    Roughly calculate how long streak is likley to have happend.

    First download games:
    python getgames.py <username>

    Get winstreak and stats:
    python calc.py <username> <optional date string>

    Allow draws in winstreak
    python calc.py -d <username> <optional date string>

    options:
      -d : allow win streaks

    <username>    = chess.com username you want to look up
    <date string> = YYYYMMDD


    If date is provided filter out all games prior to date
"""

from urllib.request import urlopen

import json
import sys
import datetime
import math
import argparse

parser = argparse.ArgumentParser("Find chess.com user longest winning streak")
parser.add_argument("username")
parser.add_argument("date", nargs='?', action='store')
parser.add_argument('-d', '--draw',
                    action='store_true')
args = parser.parse_args()
# print(args.draw)
username = args.username
epoch = 0
if args.date:
  # date  = sys.argv[2]
  year  = int( args.date[0:4])
  month = int( args.date[4:6])
  day   = int( args.date[6:8])
  epoch = int( datetime.datetime(year, month, day, 0, 0, 0).strftime('%s'))
  # print(year, month, day)

filename = "games/" + username + ".json"
with open(filename, 'r') as openfile:
  games = json.load(openfile)

all_streaks = []
all_win_chances = [] # prob user wins game at index
current = []
longest = []
draws = 0
filtered = []
for i in range(len(games)):
  # ['url', 'pgn', 'time_control', 'end_time', 'rated', 'tcn', 'uuid', 'initial_setup', 'fen', 'time_class', 'rules', 'white', 'black']
  if games[i]['white']['username'].lower() == username.lower():
    user = games[i]['white']
    opponent = games[i]['black']
  else:
    opponent = games[i]['white']
    user = games[i]['black']

  relative = user['rating'] - opponent['rating']
  odds = pow(10, relative/400)
  win_chance = odds / (odds + 1)
  games[i]['user']        = user
  games[i]['opponent']    = opponent
  games[i]['odds']        = odds
  games[i]['relative']    = relative
  games[i]['win_chance']  = win_chance

  # if date given, filter out games before date
  if epoch and games[i]['end_time'] < epoch:
    continue

  filtered.append(games[i])
  all_win_chances.append(win_chance)
  # draw_strings = [ "agreed", "repetition", "timeout", "abandoned", "50move"]
  draw_strings = [ "agreed", "repetition", "stalemate", "50move" ]
  # draw_strings = []
  if user['result'] == 'win':
    games[i]['draw'] = False
    current.append( games[i])
    if( len( current) > len( longest)):
      all_streaks.append( current)
      longest = current
  elif user['result'] in draw_strings:
    games[i]['draw'] = True
    draws += 1
    if args.draw:
      continue
    else:
      current = []
  else:
    games[i]['draw'] = False
    current = []


  # if (relative > 150) or (relative < -150) and win:
  # if (relative < -150) and win:
  #   print( "OVER UNDER " + str(relative))
  #   print('User rating '      + str(user['rating']) + ', Opponent rating '  + str(opponent['rating']))
  #   print('Relative rating '  + str(relative) + ', win_chance ' + str(win_chance))
  #   if( win):
  #     print("WE WON!!!!!!!!")
  # print(game['time_control'])

# print( "Longest streak url's:")
print("..........url.............................win chance.........time......")
for game in longest:
  # print(game['time_class'], game['url'], format(game['win_chance'], ".2%"), datetime.datetime.fromtimestamp(game['end_time']).strftime('%c'))
  print(game['url'], format(game['win_chance'], ".2%"), datetime.datetime.fromtimestamp(game['end_time']).strftime('%m/%d/%Y %H:%M:%S'))
print()
streak_prob = 1
for game in longest:
  streak_prob *= game['win_chance']
if args.draw:
  draw_text = "allowing draws: "
else:
  draw_text = "disallowing draws: "
print( "Longest streak " + draw_text + str( len(longest)) + " Probabilty of the streak happening when it happend: " + format(streak_prob, ".3%"))
print(".......................................................................")


# print( )
# prob it happens
# len(longest)


# print(all_win_chances[0:9])
# print()

# TODO: at least once, this does not work at all
# at_least_once = 0
# for i in range( len(games) - len(longest) - 1):
#   current_prob = 1
#   for prob in games[i:(i + len(longest))]:
#     current_prob *= prob['win_chance']
#   at_least_once += current_prob
# print( "Probabilty that the streaks happens at least once from the players games: ", format(at_least_once, ".3%"))

avg_win_chance = 0
for game in games:
  avg_win_chance += game['win_chance']
avg_win_chance = avg_win_chance  / len(games)

lnN = math.log(len(games))
lnP = math.log(avg_win_chance)
longest_expected = abs( lnN/lnP)
print()
print( username + " has played", len(games), "games with an avarge win chance of", format(avg_win_chance, ".1%"), "and " + str(draws) + " draws")
print("From this the longest expcted streak would be: ", int(longest_expected) , "(Roughly estimated with # of games and avg win chance)")

print()
print("Other streaks (games won, chance, date)")
for streak in all_streaks:
  prob = 1
  # print(streak);
  for game in streak:
    prob *= game['win_chance']


  print(len(streak), ",", format(prob, ".3%"), datetime.datetime.fromtimestamp(streak[0]['end_time']).strftime('%m/%d/%Y, %H:%M:%S'))