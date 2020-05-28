from typing import List, Dict
import datetime as dt
from datetime import date, timedelta
import pprint


def get_dates(date_arg):
    date_var = date_arg
    weekday = date_var.weekday()
    date_previous = date_var - timedelta(days=7)

    date_dict = {'current': date_var, 'previous': date_previous}

    def iterate_through_loop(weekday_arg, increment_decrement, is_increment = True):
        '''Lines identified in date.py that are repeated unnecessarily:
            weekday_incrementor = number
            master_list.append(date_dictionary)
            weekday_instance -= 1
            weekday_decrementor/incrementor += 1
        '''

        
        #weekday_instance -= 1
        #weekday_decrementor/incrementor += 1
        #if is_increment=True
        #     increment_decrement += 1
        #     date_dict_1 = {'current': date_var + timedelta(days=weekday_incrementor),
        #                    'previous': date_previous + timedelta(days=weekday_incrementor)}
        # else:
        #     increment_decrement -= 1
        #     date_dict_1 = {'current': date_var + timedelta(days=weekday_incrementor),
        #                    'previous': date_previous + timedelta(days=weekday_incrementor)}
        #master_list.append(date_dict)

    if weekday != 0:
        master_list = [date_dict]

    while weekday_1 > 0:
        iterate_through_loop(weekday_1, 1, is_increment=True)

    while weekday_2 < 6:
        iterate_through_loop(weekday_1, 1, is_increment=True)

    master_list_sorted = sorted(master_list, key=lambda i: i['current'])

    return master_list_sorted

 else:
        functional_date = date_var - timedelta(days=1)
        functional_date_previous = functional_date - timedelta(7)
        functional_weekday = functional_date.weekday()

        master_list_monday = []


        while functional_weekday_1 > 0:
            iterate_through_loop(date_dict_monday_1, functional_weekday, 1, is_increment=True)


        master_list_monday_sorted = sorted(master_list_monday, key=lambda i: i['current'])

        return master_list_monday_sorted

foo = get_dates(date(2020, 5, 21))
bar = get_dates(date(2020, 5, 18))
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(foo)
pp.pprint(bar)