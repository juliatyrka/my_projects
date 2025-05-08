import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

premier_league = pd.read_csv('PremierLeagueMatches.csv')

#Cleaning data
#premier_league['Attendance'] = premier_league['Attendance'].astype('int')
premier_league['Date'] = pd.to_datetime(premier_league['Date'])
premier_league['Day'] = premier_league['Date'].dt.day
premier_league['Month'] = premier_league['Date'].dt.month
premier_league['Year'] = premier_league['Date'].dt.year


#Manchester United - won matches
man_utd_home = premier_league[premier_league['Home Team'] == 'Manchester Utd']
home_won = man_utd_home[man_utd_home['homeScore'] > man_utd_home['awayScore']]
home_won_count = len(home_won)

man_utd_not_home = premier_league[premier_league['Away Team'] == 'Manchester Utd']
not_home_won = man_utd_not_home[man_utd_not_home['homeScore'] < man_utd_not_home['awayScore']]
not_home_won_count = len(not_home_won)

won_utd_matches = home_won_count + not_home_won_count
man_utd_matches = len(man_utd_home) + len(man_utd_not_home)

win_ratio_utd = round((won_utd_matches / man_utd_matches) * 100, 2)

print(f'Manchester United won {won_utd_matches} and played {man_utd_matches} matches in Premier League 2022-2025')
print(f"Win ratio is {win_ratio_utd}%")

#Expected goals

expected_utd_home_goals = round(man_utd_home['homeXG'].mean(), 2)
expected_utd_not_home_goals = round(man_utd_not_home['awayXG'].mean(), 2)
expected_mean = (expected_utd_home_goals + expected_utd_not_home_goals) / 2


#Is expected goals higher than real result?

home_goals_mean = man_utd_home['homeScore'].mean()
not_home_goals_mean = man_utd_not_home['awayScore'].mean()
goals_mean = (home_goals_mean + not_home_goals_mean) / 2

print(f'Home goals mean: {round(home_goals_mean,2)}, but expected is {expected_utd_home_goals}')
print(f'Not home goals mean: {round(not_home_goals_mean,2)}, but expected is {expected_utd_not_home_goals}')
print(f'Goals mean: {round(goals_mean,2)}, but expected is {round(expected_mean, 2)}')
