import json

with open('purchase_log.txt', 'r') as file:
    purchases = {}
    for line in file:
        data = json.loads(line)
        user_id = data['user_id']
        category = data['category']
        purchases[user_id] = category

print(purchases)
