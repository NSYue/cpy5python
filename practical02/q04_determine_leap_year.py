# Filename:q04_determine_leap_year.py
# Author: Nie Shuyue
# Date: 20130130
# Modified: 20130130
# Description: Program to determine a leap year.

# main

# Prompt and get the year
year = int(input("Enter a year: "))

# calculate and get different situation
# display the results
if year % 4 == 0 and year % 100 > 0:
    print ("Leap")

elif year % 400 == 0:
    print("Leap")

else:
    print ("Non-leap")
