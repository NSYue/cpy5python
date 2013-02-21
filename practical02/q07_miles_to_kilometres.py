# Filename:q07_miles_to_kilometres.py
# Author: Nie Shuyue
# Date: 20130204
# Modified: 20130204
# Description: Program to convert between miles and kilometers

# main

# get the title
print ( "Miles Kilometers Kilometers Miles")

# calculate and get them in table
for i in range (1,11):
    print ("{0:<5}".format (i), "{0:<9.3f}".format (i*1.609),\
           "{0:<9}".format (i*5+15), "{0:<6.3f}".format ((i*5+15)/1.609))
