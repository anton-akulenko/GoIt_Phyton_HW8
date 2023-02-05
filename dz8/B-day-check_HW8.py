from datetime import datetime, timedelta
import re

users = [
    {'name': 'Alise', 'bday': '1985-02-11'},
    {'name': 'Bob', 'bday': '1985-02-10'},
    {'name': 'Pete', 'bday': '1985-02-15'},
    {'name': 'Ivan', 'bday': '1985-02-09'},
    {'name': 'Lena', 'bday': '1985-02-12'},
    {'name': 'Ostap', 'bday': '1985-02-12'},
    {'name': 'Ksu', 'bday': '1985-02-13'},
    {'name': 'today', 'bday': '1985-02-05'},
    {'name': 'date_out_of_range', 'bday': '1985-03-05'},
]

current_date = datetime.now()
# replace(year=current_date.year)
start_of_week = current_date - timedelta(days=current_date.weekday()) + timedelta(days=7)  # відлік з понеділка
start_of_week = current_date # відлік з поточного дня
end_period = start_of_week + timedelta(days=7)
# print(re.sub(rf"^\d{4}$", str(current_date.year), "2012-12-12"))

def difference(start_of_week: datetime, end_period: datetime):
    diff = end_period - start_of_week
    days = [start_of_week + timedelta(days=i) for i in range(diff.days + 1)]
    return {d.strftime("%m-%d"): d.strftime("%Y") for d in days}

year_bd = {}
period = difference(start_of_week, end_period)

for b_person in users:

    user_bday = b_person["bday"][5:]  # take mm-dd
    if user_bday in list(period):
        d = datetime.strptime(b_person["bday"], "%Y-%m-%d").replace(year=current_date.year).strftime("%A") #create weekday + mm-dd
        if d == "Saturday":
            d = "B-day on Saturday greet on Monday"
        elif d == "Sunday":
            d = "B-day on Sunday greet on Monday"
        if not year_bd.get(d): #create dict with date + name
            year_bd[d] = [b_person['name']]
        else:
            year_bd[d].append(b_person['name'])
# print(year_bd)
for k, v in year_bd.items():
    print(f'{k} : {", ".join(v)}')

