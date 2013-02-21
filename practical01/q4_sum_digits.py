# Filename:q4_sum_digits.py
# Author: Nie Shuyue
# Date: 20130122
# Modified: 20130122
# Description: Program to get an integer between 0 and 1000
# and adds all the digits in the integer.

#main

#prompt and get the integer
integer = int(input("Enter the integer between 0 and 1000: "))

#get the sum of the last digit
sum=0
while (integer>0):
    sum+=integer%10    
# remove the extracted digit
    integer//=10
# repeat the whole function until
# all the digits are added together

# display result
print (sum)
    
