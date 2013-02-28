# Filename: q6_sum_digits.py
# Author: Nie Shuyue
# Created: 20130226
# Modified: 20130226
# Description: A recursive function to compute the sum of digits in an integer

# Function
def  sum_digits(n):
    if n < 10:
        return n
    else:
        return n%10 + sum_digits(n//10)

# main
n = int(input("Enter an integer: "))
print ("The sum of its digits is: ",sum_digits(n))




##Test
##Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
##Type "copyright", "credits" or "license()" for more information.
##>>> ================================ RESTART ================================
##>>> 
##Enter an integer: 11234
##The sum of its digits is: 11
##>>> 
