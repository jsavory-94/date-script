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

    #change target to following Sunday
    if dt.isoweekday() == 1:
        dt = dt - timedelta(days=1)
    else:
        dt = dt + timedelta(days=(7 - dt.isoweekday()))



    i = 7
    while i > 0:
        result = {'current': dt - timedelta(days=i),
                  'previous': dt - timedelta(days=i, weeks=1)}
        output.append(result)
        i-=1

    return output

foo = get_dates(date(2020, 5, 21))
bar = get_dates(date(2020, 5, 18))

print(foo)
print(bar)