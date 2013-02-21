# Filename:q06_kilograms_to_pounds.py
# Author: Nie Shuyue
# Date: 20130131
# Modified: 20130131
# Description: Program to convert kilogram to
# pounds and put them in table

# main

# get the title 
print ( "Kilograms Pounds" )

# arrange them in table form
for i in range (1,11):
    # get the values and put in correct format
    print ("{0:< 9}".format (i), "{0:<7.1f}".format (i*2.2))

