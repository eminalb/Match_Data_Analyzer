# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:53:26 2024

@author: emin

"""

import csv
import pickle

a=[]
id_teams=[1]
maks = 0
x=0
team_names= list()

with open ('Match.csv', 'r') as match:
    match_reader = csv.reader(match)
    next(match_reader)
    
    for line in match_reader:
        liste = [int(line[6]),int(line[7])]
        a.append(sorted(liste))
  
  
with open ('Match.csv', 'r') as match:
    match_reader= csv.reader(match)
    next(match_reader) 
    
    for line in match_reader:
        liste = sorted([int(line[6]),int(line[7])])
        x = a.count(liste)
        
        if x > maks:
            maks=x
            id_teams[0] = liste

for team in id_teams:
    final_list= team

with open ('Team.csv', encoding="utf-8") as team_csv:
    team_reader= csv.reader(team_csv)
    next(team_reader)
    for line in team_reader:
            if final_list[0]==int(line[0]) or final_list[1]==int(line[0]):
                team_names.append(line[1])


with open('query3.pickle','wb') as pickle_file:
    pickle.dump(team_names, pickle_file)
    