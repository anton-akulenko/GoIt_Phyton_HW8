from datetime import datetime, timedelta

users = [
    {'name': 'Alise', 'bday': '1985-02-11'},
    {'name': 'Bob', 'bday': '1985-02-10'},
    {'name': 'Pete', 'bday': '1985-02-08'},
    {'name': 'Ivan', 'bday': '1985-02-09'},
    {'name': 'Lena', 'bday': '1985-02-12'},
    {'name': 'Ostap', 'bday': '1985-02-12'},
    {'name': 'Ksu', 'bday': '1985-02-13'},
    {'name': 'date_out_of_range', 'bday': '1985-02-05'},
    {'name': 'date_out_of_range2', 'bday': '1985-03-05'},
]

current_date = datetime.now()

start_of_week = current_date - timedelta(days=current_date.weekday()) + timedelta(days=7)  # option 1
end_period = start_of_week + timedelta(days=7)


def difference(start_of_week: datetime, end_period: datetime):
    diff = end_period - start_of_week
    days = [start_of_week + timedelta(days=i) for i in range(diff.days + 1)]
    return {d.strftime("%m-%d"): d.strftime("%Y") for d in days}

year_bd = {}
period = difference(start_of_week, end_period)

for b_person in users:

    user_bday = b_person["bday"][5:]  # take mm-dd
    if user_bday in list(period):
        d = datetime.strptime(b_person["bday"], "%Y-%m-%d").strftime("%A (%m-%d)") #create weekday + mm-dd
        if not year_bd.get(d): #create dict with date + name
            year_bd[d] = [b_person['name']]
        else:
            year_bd[d].append(b_person['name'])
# print(year_bd)
for k, v in year_bd.items():
    print(f'On {k} birthdays has: {", ".join(v)}')

