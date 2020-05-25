from typing import List, Dict
import datetime as dt
from datetime import date, timedelta
import pprint


def get_dates(date_arg):
    '''
        Params
            date_arg: a date in format datetime

        Returns:
            master_list_sorted:  list of dates within
            a week that includes the given date, plus matching day
            from the previous week. If a Monday date is provided,'current' dates
            will be the previous week, not the week that includes the Monday date
        '''

    date_var = date_arg
    weekday = date_var.weekday()

    if weekday != 0:  # non-monday date logic
        date_previous = date_var - timedelta(days=7)

        date_dict = {'current': date_var, 'previous': date_previous}

        master_list = [date_dict]

        weekday_1 = weekday  # for reference in logic generating dicts before date given
        weekday_decrementor = 1

        # Create and append dicts of date before given
        while weekday_1 > 0:
            date_dict_new = {'current': date_var - timedelta(days=weekday_decrementor),
                             'previous': date_previous - timedelta(days=weekday_decrementor)}
            master_list.append(date_dict_new)
            weekday_1 -= 1
            weekday_decrementor += 1

        weekday_2 = weekday  # for reference in logic generating dicts after date given
        weekday_incrementor = 1

        ## Create and append dicts of date after given
        while weekday_2 < 6:
            date_dict_new_1 = {'current': date_var + timedelta(days=weekday_incrementor),
                               'previous': date_previous + timedelta(days=weekday_incrementor)}
            master_list.append(date_dict_new_1)
            weekday_2 += 1
            weekday_incrementor += 1

        master_list_sorted = sorted(master_list, key=lambda i: i['current'])

        return master_list_sorted



    else:  # non-monday logic
        functional_date = date_var - timedelta(days=1)  # previous sunday to monday date given
        functional_date_previous = functional_date - timedelta(7)
        functional_weekday = functional_date.weekday()
        functional_weekday_incrementor = 1

        functional_weekday_1 = functional_weekday

        master_list_monday = []

        # Create and append dates from previous week
        while functional_weekday_1 > 0:
            date_dict_monday = {'current': functional_date, 'previous': functional_date_previous}
            date_dict_monday_1 = {'current': functional_date - timedelta(days=functional_weekday_incrementor),
                                  'previous': functional_date_previous - timedelta(days=functional_weekday_incrementor)}

            if functional_weekday_1 == 6:
                master_list_monday.append(date_dict_monday)

            master_list_monday.append(date_dict_monday_1)
            functional_weekday_1 -= 1
            functional_weekday_incrementor += 1

        master_list_monday_sorted = sorted(master_list_monday, key=lambda i: i['current'])

        return master_list_monday_sorted


foo = get_dates(date(2020, 5, 21))
bar = get_dates(date(2020, 5, 18))
pp = pprint.PrettyPrinter(indent=1)
print('---foo: 2020, 5, 21---')
pp.pprint(foo)
print('---bar: 2020, 5, 18---')
pp.pprint(bar)
