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


#Збереження оновленого масиву
columns = ["transaction_id", "date", "region", "product_category", "quantity", "revenue", "net_profit"]
with open("cleaned_sales_updated.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(list_of_dictionaries)

# Аналітика (Новий масив даних)
category_net_profit = {}
for a in list_of_dictionaries:
    category_net_profit[a["product_category"]] = 0

with open("cleaned_sales_updated.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        for key, value in category_net_profit.items():
            if key == row["product_category"]:
                category_net_profit[key] += float(row["net_profit"])
print(category_net_profit)

#Cередній прибуток
all_net_profit = 0
for key, value in category_net_profit.items():
    all_net_profit += value
average_net_profit = all_net_profit / len(category_net_profit)
category_net_profit_more_than_average = dict(filter(lambda row: row[1]>=average_net_profit, category_net_profit.items()))
print(category_net_profit_more_than_average)

#Відсортування категорій
new_category_list = dict(sorted(category_net_profit_more_than_average.items(), key=lambda x: x[1], reverse=True))
print(new_category_list)