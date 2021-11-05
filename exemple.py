from datetime import datetime, timedelta, date
from calendar import monthrange
from dateutil import relativedelta as rdelta

# data_input = input('Введите дату рождения: ')
#
# date_of_birth = datetime.strptime(data_input, '%m, %d, %Y')
# print(f'{date_of_birth.month} - {date_of_birth.day} - {date_of_birth.year}')
#
# current_date = datetime.now()
# f = datetime.strftime(current_date, '%m - %d - %Y')
# print(f)
#
# delta = abs((current_date - date_of_birth).days)
# print(delta)


def monthdelta(input_date):
    now = datetime.strftime(datetime.now(), '%Y - %m - %d').split('-')
    current_date = date(int(now[0]), int(now[1]), int(now[2]))

    split_input_data = input_date.split('-')
    date_of_birth = date(int(split_input_data[0]), int(split_input_data[1]), int(split_input_data[2]))

    delta = 0
    cal_date = date_of_birth
    while True:
        mdays = monthrange(cal_date.year, cal_date.month)[1]
        cal_date += timedelta(days=mdays)
        if cal_date <= current_date:
            delta += 1
        else:
            break
        rd = rdelta.relativedelta(current_date, date_of_birth)

        return f"{rd.years} years, {rd.months} months by outer module, {delta} by calendar module"


print(monthdelta(input("Введите дату рождения: ")))







