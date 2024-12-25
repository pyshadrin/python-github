import datetime

# Форматирование дат для каждой газеты
def format_newspaper_date(newspaper, date_string):
    if newspaper == 'The Moscow Times':
        return datetime.datetime.strptime(date_string, '%A, %B %d, %Y')
    elif newspaper == 'The Guardian':
        return datetime.datetime.strptime(date_string, '%A, %d.%m.%y')
    elif newspaper == 'Daily News':
        return datetime.datetime.strptime(date_string, '%A, %d %B %Y')

# Пример работы программы
moscow_times_date = format_newspaper_date('The Moscow Times', 'Wednesday, October 2, 2002')
print(f"The Moscow Times: {moscow_times_date}")

guardian_date = format_newspaper_date('The Guardian', 'Friday, 11.10.13')
print(f"The Guardian: {guardian_date}")

daily_news_date = format_newspaper_date('Daily News', 'Thursday, 18 August 1977')
print(f"Daily News: {daily_news_date}")
