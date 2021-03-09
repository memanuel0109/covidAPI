import requests
import json

import matplotlib.pyplot as plt


url = 'https://api.covidtracking.com/v1/us/daily.json'
response = requests.get(url)

json_data = response.json()


import pandas as pd


d = {}
for item in list(json_data[0].keys()):
	array = []
	for i in range(len(json_data)):
		array.append(json_data[i][str(item)])
		d.update({item:array})

df = pd.DataFrame.from_dict(d)
df['date'] = df['date'].astype(str)

def split_date(date):
    """reformat the dates"""
    for _ in date:
        return '{}{}{}{}-{}{}-{}{}'.format(date[0], date[1], date[2], date[3], date[4], date[5], date[6], date[7])

df['date'] = [*map(lambda x: split_date(x), df['date'])]

df['date'] = pd.to_datetime(df['date'])

df.to_csv('covid_data.csv')


fig, ax = plt.subplots(figsize=(16,12))

ax.plot(df['date'], df['positive'])
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title('Cumulative Sum of the Number of Cases Over Time')

plt.savefig('cases.jpg')


fig, ax = plt.subplots(figsize=(16,12))

ax.plot(df['date'], df['death'], color='red')
plt.xlabel('Date')
plt.ylabel('Number of Deaths')
plt.title('Cumulative Sum of the Number of Deaths Over Time')

plt.savefig('deaths.jpg')