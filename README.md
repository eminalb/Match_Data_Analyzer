# Football Data Analysis Project

This project consists of three Python scripts (query1.py, query2.py, and query3.py) that analyze football match data to extract specific insights. The scripts process data from CSV files, perform various analyses, and save the results as pickle files.


## Project Structure

query1.py: Analyzes the top goal scorers for each team across multiple seasons.


query2.py: Identifies the top 50 players with the most yellow cards.


query3.py: Finds the most frequent match-ups between teams.


## Data Files

1) Match.csv: Contains match data, including match incidents, teams, and other relevant details.

2) Team.csv: Contains team information, such as team IDs and names.

3) Country.csv: Contains countries and their IDs.

4) League.csv: Contains league IDs, country IDs and league names.

5) Player.csv: Contains player features such as IDs, name, height and birthday.

6) PlayerAttributes.csv: Contains player attributes such as overall rating, finishing, accuracy, etc.

7) TeamAttributes.csv: Contains team attributes such as play speed, dribbling class, play passing, etc. 


## Script Details

### query1.py

This script identifies the top goal scorers for each team across multiple seasons (from 2008/2009 to 2015/2016). 
It processes the Match.csv file to extract goal-scoring incidents and counts the number of goals scored by each player for each team.
The results are saved in a dictionary where the keys are team IDs and the values are lists of player IDs who scored the most goals. 
The final result is saved as query1.pickle.


### query2.py

This script identifies the top 50 players with the most yellow cards across all matches. 
It processes the Match.csv file to extract yellow card incidents and counts the number of yellow cards received by each player. 
The results are saved as a list of tuples, where each tuple contains a player ID and the number of yellow cards they received. 
The final result is saved as query2.pickle.



### query3.py

This script identifies the most frequent match-ups between teams. 
It processes the Match.csv file to count how often each pair of teams has played against each other. 
The most frequent match-up is identified, and the corresponding team names are extracted from the Team.csv file. 
The final result is saved as query3.pickle.



## Usage

Ensure that the required data files (Match.csv and Team.csv) are in the same directory as the scripts.


Run each script using Python:
```python query1.py```
```python query2.py```
```python query3.py```.
The results will be saved as pickle files.


## Output Files
query1.pickle: Contains a dictionary of top goal scorers for each team.

query2.pickle: Contains a list of the top 50 players with the most yellow cards.

query3.pickle: Contains the names of the teams involved in the most frequent match-up.
