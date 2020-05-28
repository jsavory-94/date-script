"""

I want a function, that given a date, returns a list of dates within
a week that includes the given date, plus the matching day
from the previous week

E.g. if `date(2020, 5, 21)` was entered-- the returned data would be:

[
    {'current': date(2020, 5, 18), 'previous': date(2020, 5, 11)},
    {'current': date(2020, 5, 19), 'previous': date(2020, 5, 12)},
    {'current': date(2020, 5, 20), 'previous': date(2020, 5, 13)},
    {'current': date(2020, 5, 21), 'previous': date(2020, 5, 14)},
    {'current': date(2020, 5, 22), 'previous': date(2020, 5, 15)},
    {'current': date(2020, 5, 23), 'previous': date(2020, 5, 16)},
    {'current': date(2020, 5, 24), 'previous': date(2020, 5, 17)},
]

One caveat is, if a Monday date is provided, I want the 'current' dates
to be the previous week, not the week that includes the Monday date, e.g:

Provided date: `date(2020, 5, 18)` returned data:

[
    {'current': date(2020, 5, 11), 'previous': date(2020, 5, 4)},
    {'current': date(2020, 5, 12), 'previous': date(2020, 5, 5)},
    {'current': date(2020, 5, 13), 'previous': date(2020, 5, 6)},
    {'current': date(2020, 5, 14), 'previous': date(2020, 5, 7)},
    {'current': date(2020, 5, 15), 'previous': date(2020, 5, 8)},
    {'current': date(2020, 5, 16), 'previous': date(2020, 5, 9)},
    {'current': date(2020, 5, 17), 'previous': date(2020, 5, 10)},
]


"""

from typing import List, Dict
from datetime import date


def get_dates(dt: date) -> List[Dict[str, date]]:
    ...
    placeholder_data = [
        {"current": date(2020, 1, 1), "previous": date(2020, 1, 1)},
        ...,
    ]
    return placeholder_data


# Results of these should align with the details in the notes above.

foo = get_dates(date(2020, 5, 21))
print(foo)

bar = get_dates(date(2020, 5, 18))
print(bar)
