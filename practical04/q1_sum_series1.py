# Filename: q1_sum_series1.py
# Author: Nie Shuyue
# Created: 20130222
# Modified: 20130222
# Description: A recursive function to compute a series.

# Function
def sum_series1(i):
    if i == 1 :
        return 1
    else:
        return sum_series1(i-1)+ 1/i
# main
i = int(input("Enter an integer: "))
print(sum_series1(i))


##TEST
##Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
##Type "copyright", "credits" or "license()" for more information.
##>>> ================================ RESTART ================================
##>>> 
##Enter an integer: 4
##2.083333333333333
##>>> 
