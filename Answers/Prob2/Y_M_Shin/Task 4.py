# -*- coding: utf-8 -*-
"""
Task 4
"""
import datetime as dt

now = dt.datetime.now() # Current date
nowdate = now.strftime('%Y-%m-%d') # Curent date with only Year/Month/Date
print("Today is", nowdate)

n = int(input("How many days do you wish to go by?: "))

destination = now + dt.timedelta(days = n) # Add n days from current date
destinationdate = destination.strftime('%Y-%m-%d')
print(n, "days from today is", destinationdate)