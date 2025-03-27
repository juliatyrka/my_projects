import pandas as pd
import numpy as np

schools = pd.read_csv('schools.csv')
print(schools.head())
print('-------------------')

#Finding schools with the best math scores (threshold 80% of max points, 640/800)
sorted_math_schools = schools.sort_values('average_math', ascending=False)
best_math_schools = sorted_math_schools[sorted_math_schools['average_math'] >= 640]
best_math_schools = best_math_schools[['school_name', 'average_math']]

print(best_math_schools.head())
print('-------------------')
#Top 10
schools['total_SAT'] = schools["average_math"] + schools["average_writing"] + schools["average_reading"]
sorted_sat = schools.sort_values('total_SAT', ascending=False)

top_10 = sorted_sat.head(10)
print(top_10)
print('-------------------')

#Locating the NYC borough with the largest standard deviation in SAT performance
boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"])
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})