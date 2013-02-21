# Filename:q1_fahrenheit_to_celsius.py
# Author: Nie Shuyue
# Date: 20130121
# Modified: 20130121
# Description: Program to convert Fahrenheit to Celsius

# main

# prompt and get Fahrenheit input
fahrenheit = float(input("Enter Degree in Fahrenheit :"))

# converts Fahrenheit to Celsius
celsius = (5/9) * (fahrenheit - 32)


# display result
print ("Celsius degree={0:.0f}".format(celsius))
