import csv
import json

list_of_dictionaries = []
with open("global_sales.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        list_of_dictionaries.append(row)

with open("regional_tariffs.json", "r", encoding="utf-8") as file:
    dictionary = json.load(file)

# Очищення даних
for row in list_of_dictionaries:
    if row["quantity"] == "N/A":
        row["quantity"] = 0
    else:
        row["quantity"] = int(row["quantity"])

    if row["revenue"] == "N/A":
        row["revenue"] = 0
    else:
        row["revenue"] = float(row["revenue"])


for key, val in dictionary.items():
    if val == "N/A":
        dictionary[key] = 0
    else:
        dictionary[key] = float(val)

#Оновлення даних
for row in list_of_dictionaries:
    for a in dictionary:
        if a == row["region"]:
            row["net_profit"] = row["revenue"] - (row["revenue"] * (dictionary[a]/100))
print(list_of_dictionaries)

