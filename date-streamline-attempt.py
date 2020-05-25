from typing import List, Dict
import datetime as dt
from datetime import date, timedelta
import pprint


def get_dates(date_arg):
    date_var = date_arg
    weekday = date_var.weekday()
    date_previous = date_var - timedelta(days=7)

    date_dict = {'current': date_var, 'previous': date_previous}

    def iterate_through_loop(dictionary date, weekday_arg, increment, is_increment = True):
        weekday_local = weekday

        if is_incrementor=True
            increment += 1

        else:
            increment -= 1

if weekday != 0:
    master_list = [date_dict]

    weekday_1 = weekday
    weekday_decrementor = 1

    while weekday_1 > 0:
        iterate_through_loop(date_dict, weekday_1, 1, is_increment=True)

    date_dict_new_1 = {'current': date_var + timedelta(days=weekday_incrementor),
                       'previous': date_previous + timedelta(days=weekday_incrementor)}

    while weekday_2 < 6:
        iterate_through_loop(date_dict, weekday_1, 1, is_increment=True)

master_list_sorted = sorted(master_list, key=lambda i: i['current'])

return master_list_sorted

else:
functional_date = date_var - timedelta(days=1)
functional_date_previous = functional_date - timedelta(7)
functional_weekday = functional_date.weekday()
functional_weekday_incrementor = 1

functional_weekday_1 = functional_weekday

master_list_monday = []

date_dict_monday_1 = {'current': functional_date - timedelta(days=functional_weekday_incrementor),
                          'previous': functional_date_previous - timedelta(days=functional_weekday_incrementor)}

while functional_weekday_1 > 0:
    iterate_through_loop(date_dict_monday_1, functional_weekday, 1, is_increment=True)


master_list_monday_sorted = sorted(master_list_monday, key=lambda i: i['current'])

return master_list_monday_sorted

foo = get_dates(date(2020, 5, 21))
bar = get_dates(date(2020, 5, 18))
pp = pprint.PrettyPrinter(indent=1)
print('---foo: 2020, 5, 21---')
pp.pprint(foo)
print('---bar: 2020, 5, 18---')
pp.pprint(bar)
