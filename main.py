import csv
import json


# Функция для перевода дюймов в сантиметры
def convert_inches_to_sm(height_inches):
    return round(height_inches * 2.54)


# Функция для перевода фунтов в килограммы
def convert_ibs_kg(weight_lbs):
    return round(weight_lbs * 0.453592)


def csv_to_json(csvFilePath, jsonFilePath):
    data = []

    with open(csvFilePath, 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if all(row.values()):
                row = {k.strip('"').strip(): v.strip('"').strip() for k, v in row.items()}

                row.pop("Team", None)

                row['Height'] = convert_inches_to_sm(float(row.pop('Height(inches)')))
                row['Weight'] = convert_ibs_kg(float(row.pop('Weight(ibs)')))

                row['Age'] = int(float(row['Age']))

                data.append(row)

    with open(jsonFilePath, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=1)


csvFilePath = 'mlb_players.csv'
jsonFilePath = 'data.json'
csv_to_json(csvFilePath, jsonFilePath)