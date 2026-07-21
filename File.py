import csv
import json

list_of_dictionaries = []
with open("global_sales.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        list_of_dictionaries.append(row)


with open("regional_tariffs.json", "r", encoding="utf-8") as file:
    dictionary = json.load(file)
print(dictionary)