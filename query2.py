# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:34:18 2024

@author: emin
"""
import csv
import json
import operator
import pickle
from collections import OrderedDict

final_incidents = list()
players_yellow = dict()


with open('Match.csv', 'r') as match:
    match_reader = csv.reader(match)
    next(match_reader)
    
    for line in match_reader:
        if len(line[34])>0 and len(line[34]) != 16:
            final_incidents.append(line[34])

for single_match in final_incidents:
    single_match = json.loads(single_match)
    for incident in single_match:
        try:
            if incident["card_type"] == "y" or incident["card_type"] == "y2":
                players_yellow[incident["player1"]] = 0 
        except:
            KeyError
for single_match in final_incidents:
    single_match = json.loads(single_match)
    for incident in single_match:
        try:
            if incident["card_type"] == "y":
                players_yellow[incident["player1"]] += 1
            if incident["card_type"] == "y2":
                players_yellow[incident["player1"]] += 2
        except:
            KeyError

sorted_players_yellow= dict(sorted(players_yellow.items(),key=operator.itemgetter(1)))
reverse = OrderedDict(reversed(list(sorted_players_yellow.items())))
reversed_players_yellow = dict(list(reverse.items())[:50])
final_list= list(reversed_players_yellow.items())


with open('query2.pickle','wb') as pickle_file:
    pickle.dump(final_list, pickle_file)
    