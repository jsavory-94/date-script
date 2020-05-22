from typing import List, Dict
import datetime as dt
from datetime import date, timedelta
import pprint

def get_dates(yr, mo, day):
   date_str = f'{yr}-{mo}-{day}'
   date = dt.datetime.strptime(date_str, '%Y-%m-%d')
   weekday = date.weekday()
   #print(weekday)


   if weekday != 0:
      print('non-monday code running')
      date_previous = date - timedelta(days=7)
      date_previous_str = date_previous.strftime('%Y-%m-%d')
      date_previous = dt.datetime.strptime(date_previous_str, '%Y-%m-%d')
      # print('L15')
      # print(type(date_previous))

      date_dict = {'current': date, 'previous': date_previous}
      # print(weekday)


      master_list = [date_dict]



      weekday_1 = weekday
      weekday_decrementor = 1


      while weekday_1 > 0:
         #print(weekday_decrementor)
         #print('finding previous monday to time given')
         date_dict_new = {'current': date - timedelta(days=weekday_decrementor), 'previous': date_previous - timedelta(days=weekday_decrementor)}
         #print(date_dict_new)
         ##print(date_dict_new['previous'])
         #print(type(date_dict_new['previous']))
         # print(date_dict_new)
         master_list.append(date_dict_new)
         #print(f'current weekday {weekday_1}')
         weekday_1 -= 1
         weekday_decrementor +=1


      weekday_2 = weekday
      weekday_incrementor = 1

      while weekday_2 < 6:
         #print(weekday_decrementor)
         #print('finding next Sunday to time given')
         date_dict_new_1 = {'current': date + timedelta(days=weekday_incrementor), 'previous': date_previous + timedelta(days=weekday_incrementor)}
         #print(date_dict_new_1)
         # print(date_dict_new)
         master_list.append(date_dict_new_1)
         #print(f'current weekday {weekday_2}')
         weekday_2 += 1
         weekday_incrementor +=1

      # print(master_list)

      master_list_sorted = sorted(master_list, key=lambda i: i['current'])

      return master_list_sorted



   else:
      print('Monday code running')
      functional_date = date - timedelta(days=1)
      functional_date_previous = functional_date - timedelta(7)
      functional_weekday = functional_date.weekday()
      functional_weekday_incrementor = 1

      print(f'functional date: {functional_date}')
      print(functional_date_previous)
      print(functional_weekday)




      functional_weekday_1 = functional_weekday

      master_list_monday = []

      while functional_weekday_1 > 0:
         print(functional_weekday_1)

         date_dict_monday = {'current': functional_date, 'previous': functional_date_previous}
         date_dict_monday_1 = {'current': functional_date - timedelta(days=functional_weekday_incrementor), 'previous': functional_date_previous - timedelta(days=functional_weekday_incrementor)}
         print(date_dict_monday)
         ##print(date_dict_new['previous'])
         #print(type(date_dict_new['previous']))
         # print(date_dict_new)
         if functional_weekday_1 == 6:
            master_list_monday.append(date_dict_monday)

         master_list_monday.append(date_dict_monday_1)
         #print(f'current weekday {weekday_1}')
         functional_weekday_1 -= 1
         functional_weekday_incrementor +=1

      master_list_monday_sorted = sorted(master_list_monday, key=lambda i: i['current'])


      return master_list_monday_sorted


      # master_list_new = []
      #
      # format_loop_counter = 0

   #    for m in master_list:
   #       print('list format loop is running')
   #       print(f'format loop iteration: {format_loop_counter}')
   #       print(type(m['current']))
   #       print(type(m['previous']))
   #
   #       current_new = m['current'].strftime('%Y-%m-%d')
   #
   #       previous_new = m['previous']
   #       # previous_new = dt.datetime.strptime(previous_new_str, '%Y-%m-%d')
   #
   #       print('L51')
   #
   #       #previous_new = m['previous'].strftime('%Y-%m-%d')
   #
   #       master_list_new.append(current_new)
   #       master_list_new.append(previous_new)
   #
   #       format_loop_counter += 1
   #
   #       print(master_list_new)
   #
   #    #on second loop,
   #
   #
   # else:
   #    print('monday logic goes here')


foo = get_dates(2020,5,21)
bar = get_dates(2020, 5, 18)


pp = pprint.PrettyPrinter(indent=1)

print('---2020, 5, 21---')
pp.pprint(foo)

print('---2020, 5, 18---')
pp.pprint(bar)