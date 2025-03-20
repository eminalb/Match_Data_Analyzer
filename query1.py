# -*- coding: utf-8 -*-
"""

"""


import csv
import json
import pickle
from collections import Counter


match1= list()


def top_scorer(year):
    with open('Match.csv','r') as match:
        match_reader=csv.reader(match)
        next(match)
        king = dict()
        king_league = {}
        for line in match_reader:
            if line[2]== year:
                if len(line[32])>0 and len(line[32])!=16:
                    match1= json.loads(line[32])
                    
                    for incident in match1:
                        try: 
                            key= (incident['player1']),(line[1])
                            
                            king[key] = king.get(key, 0) + 1
                            
                        except:    
                            KeyError
                king = dict(sorted(king.items(), key=lambda item: item[1], reverse=False))
    for key in king:
        king_league[key[1]]= key[0]
    return king_league


year2008 = top_scorer("2008/2009")
year2009 = top_scorer("2009/2010")
year2010 = top_scorer("2010/2011")
year2011 = top_scorer("2011/2012")
year2012 = top_scorer("2012/2013") 
year2013 = top_scorer("2013/2014")
year2014 = top_scorer("2014/2015")
year2015 = top_scorer("2015/2016")
    


all_years = [year2008,year2009,year2010,year2011,year2012,year2013,year2014,year2015]

flat_values = [item for year in all_years for item in year.values()]
counter = Counter(flat_values)

goal_kings_dict = {}
for year, goals in zip(range(2008, 2016), all_years):
    for team_id, player_id in goals.items():
        if counter[player_id] >= 2:
            if team_id not in goal_kings_dict:
                goal_kings_dict[team_id] = {player_id}
            else:
                goal_kings_dict[team_id].add(player_id)

all_teams = set(team_id for goals in all_years for team_id in goals.keys())
for team_id in all_teams:
    if team_id not in goal_kings_dict:
        goal_kings_dict[team_id] = None
        
final_result = {team_id: list(players) if players else None for team_id, players in goal_kings_dict.items()}



with open('query1.pickle','wb') as pickle_file:
    pickle.dump(final_result, pickle_file)
    
    


    