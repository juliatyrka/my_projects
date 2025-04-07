import pandas as pd
from matplotlib import pyplot as plt

super_bowls = pd.read_csv('super_bowls.csv')
tv = pd.read_csv('tv.csv')
halftime_musicians = pd.read_csv('halftime_musicians.csv')

#Identifying the year with the highest viewership
plt.plot(tv.super_bowl, tv.avg_us_viewers)
plt.title('Average Number of US Viewers')
plt.show()
print(f"Super Bowl viewership increased over time.")
viewership_increased = True

#How many matches finished with a point difference greater than 40?
difference = len(super_bowls[super_bowls['difference_pts'] > 40])
print(f"Matches finished with a point difference greater than 40: {difference}.")

plt.hist(super_bowls.difference_pts)
plt.show()

#Finding most frequent performers
performer = halftime_musicians.groupby('musician').sum('num_songs')
performer = performer.sort_values('num_songs', ascending=False)

most_songs = performer.index[0]
print(f"Most frequent performer is {most_songs}.")