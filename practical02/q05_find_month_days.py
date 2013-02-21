# Filename:q05_find_month_days.py
# Author: Nie Shuyue
# Date: 20130130
# Modified: 20130130
# Description: Program to get the
# number of days in a month of a year.

# main

# prompt and get the month and the year
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# state different conditions
# and display the resluts
if month == 1 or month == 3 or month == 5 or month == 7 \
or month == 8 or month == 10 or month == 12:
    print("31")
    
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30")
    
elif month == 2 and year % 4 == 0 and year % 100 > 0 or year% 400==0:
    print("29")

else:
    print("28")
