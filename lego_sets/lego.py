import pandas as pd
from pandas import pivot_table

lego_sets = pd.read_csv('lego_sets.csv')
parent_themes = pd.read_csv('parent_themes.csv')

lego_sets_clean = lego_sets.dropna(subset=['set_num','name','theme_name'])

#list of licensed sets
licensed_list = parent_themes[parent_themes['is_licensed']]['name']

licensed = lego_sets_clean['parent_theme'].isin(licensed_list)
licensed_sets = lego_sets_clean[licensed]


#Percentage of Star Wars themed sets
b = len(lego_sets[lego_sets['parent_theme']=='Star Wars'])
a = len(licensed_sets)
ratio = b/a
the_force = int(ratio * 100)
print(f'The percentage of licensed sets that are Star Wars themed is {the_force}%.')


#Finding the year when the most Star Wars were released
#pivot table to count total number of sets

table = pivot_table(lego_sets, values='set_num', columns='parent_theme', aggfunc='count', index='year')
table = table.fillna(0)
table = table['Star Wars'].sort_values(ascending=False)
print(table.head())
new_era = 2016
print(f'The year when the most Star Wars sets were released was {new_era}.')


