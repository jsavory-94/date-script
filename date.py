from typing import List, Dict
import datetime as dt
from datetime import date, timedelta

def get_dates(yr, mo, day):
   date_str = f'{yr}-{mo}-{day}'
   date = dt.datetime.strptime(date_str, '%Y-%m-%d')
   weekday = date.weekday()


   if weekday != 0:
      date_previous_str = date - timedelta(days=7)
      date_previous_str_formatted = date_previous_str.strftime('%Y-%m-%d')

      date_previous = dt.datetime.strptime(date_str, '%Y-%m-%d')
      # print('L15')
      # print(type(date_previous))

      date_dict = {'current': date, 'previous': date_previous_str_formatted}
      # print(weekday)


      master_list = [date_dict]

      i=weekday
      weekday_decrementor = 1
      #print(i)

      while i > 0:
         #print(weekday_decrementor)
         # print('while loop is running')
         date_dict_new = {'current': date - timedelta(days=weekday_decrementor), 'previous': date_previous - timedelta(days=weekday_decrementor)}
         # print(date_dict_new)
         master_list.append(date_dict_new)
         i -= 1
         weekday_decrementor +=1

      # print(master_list)
      return master_list


   else:
      print('Monday code goes here')
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


get_dates(2020,5,21)