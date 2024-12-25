import json
import csv

# Чтение purchase_log.txt и создание словаря purchases
with open('purchase_log.txt', 'r') as file:
    purchases = {}
    for line in file:
        data = json.loads(line)
        user_id = data['user_id']
        category = data['category']
        purchases[user_id] = category

# Обработка visit_log.csv и запись в funnel.csv
with open('visit_log.csv', 'r') as visit_file, open('funnel.csv', 'w') as funnel_file:
    reader = csv.reader(visit_file)
    writer = csv.writer(funnel_file)
    
    # Проход по строкам visit_log.csv
    for row in reader:
        user_id = row[0]
        if user_id in purchases:
            category = purchases[user_id]
            # Добавление категории в visit_log.csv
            row.append(category)
            
            # Запись строки в funnel.csv
            writer.writerow(row)

print("Содержимое funnel.csv:")
with open('funnel.csv', 'r') as funnel_file:
    for row in csv.reader(funnel_file):
        print(row)
