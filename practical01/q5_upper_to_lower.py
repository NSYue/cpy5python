# Filename:q5_upper_to_lower.py
# Author: Nie Shuyue
# Date: 20130122
# Modified: 20130122
# Description: Program to convert an uppercase letter
# from standard input to a lowercase letter

#main

#prompt and get uppercase letters
up = input("Enter uppercase letters : ")

#convert the uppercase letter to lowercase letter
low=(chr(ord(up)+32))

#display result
print ("The lowercase letter :" ,low)
