# Filename: q8_convert_milliseconds.py
# Author: Nie Shuyue
# Created: 20130221
# Modified: 20130221
# Description: Program to convert milliseconds to hours, nimutes and seconds.

# Function
def convert_ms(n):
    hours = n//3600000
    n %= 3600000
    minutes = n//60000
    n %= 60000
    seconds = n//1000

    print (hours,":",minutes,":",seconds)

# main
n = int(input("Enter the number of milliseconds: "))
convert_ms(n)
