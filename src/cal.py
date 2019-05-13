"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

# Datetime examples: https://www.pythonforbeginners.com/basics/python-datetime-time-examples

import sys
import calendar
# "from datetime import datetime" only imports the datetime class of datetime, making it incapalbe of using .date.today() and other methods
# best to import datetime completed; but could also do: from datetime import datetime, date
import datetime
import time
# How to use time and datetime: https://www.programiz.com/python-programming/datetime/strftime

def getDate(*dates):
  year = int(datetime.date.today().strftime('%Y'))
  month = int(datetime.date.today().strftime('%m'))

  if(len(dates) == 0):
    # return current month
    print('current month: ', datetime.date.today())
    calendar.prmonth(year, month)
  
  elif(len(dates) == 1):
    # return month specified
    calendar.prmonth(year, dates[0])
  
  elif(len(dates) == 2):
    # return month and year specified
    calendar.prmonth(dates[1], dates[0])
  
  else:
    # return proper syntax
    print('Please enter a valid month (1-12), optionally followed by a valid year.')
  
getDate()
getDate(12)
getDate(2, 2015)
getDate(8, 2009, 0)