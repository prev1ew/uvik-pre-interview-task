import csv
import json


result = dict()
with open('data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for num, row in enumerate(csvreader):
        if not num:  # if n = 0
            continue
        city, human_name = row
        if city not in result:
            result[city] = dict()
            result[city]['people'] = list()
        result[city]['people'].append(human_name)

for row in result.values():
    row['count'] = len(row['people'])

print(json.dumps(result, indent=2, default=str))
