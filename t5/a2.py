import datetime

def date_range(start_date, end_date):
    if start_date == '' or end_date == '':
        return []
    
    try:
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return []
    
    if start_date > end_date:
        return []
    
    current_date = start_date
    dates = []
    while current_date <= end_date:
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += datetime.timedelta(days=1)
    
    return dates

# Примеры работы программы
start_date = '2022-01-01'
end_date = '2022-01-03'
result = date_range(start_date, end_date)
print(result)

start_date = '2022-01-03'
end_date = '2022-01-01'
result = date_range(start_date, end_date)
print(result)

start_date = '2022-01-01'
end_date = '2022-01-01'
result = date_range(start_date, end_date)
print(result)
