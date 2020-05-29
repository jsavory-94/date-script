from typing import List, Dict
import datetime as dt
from datetime import date, timedelta
import pprint


def get_dates(dt):
    output = []
    """
        Params
            date_arg: a date in format datetime

        Returns:
            master_list_sorted:  list of dates within
            a week that includes the given date, plus matching day
            from the previous week. If a Monday date is provided,'current' dates
            will be the previous week, not the week that includes the Monday date
        """


    if dt.isoweekday() == 1:  #change dt to previous Sunday
        dt = dt - timedelta(days=1)
    else:
        dt = dt + timedelta(days=(7 - dt.isoweekday())) #change target to following Sunday

    for x in reversed(range(7)):
        result = {
            "current": dt - timedelta(days=x),
            "previous": dt - timedelta(days=x, weeks=1),
        }
        output.append(result)

    return output

foo = get_dates(date(2020, 5, 21))
bar = get_dates(date(2020, 5, 18))

print(foo)
print(bar)