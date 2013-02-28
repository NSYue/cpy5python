# Filename: q2_sum_series2.py
# Author: Nie Shuyue
# Created: 20130222
# Modified: 20130222
# Description: A recursive function to compute a series.

# Function
def sum_series2(i):
    if i ==0:
        return 0
    else:
        return i/(2*i+1) + sum_series2(i-1)

# main
i = int(input("Enter an ingeter i: "))
print (sum_series2(i))


##TEST
##Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
##Type "copyright", "credits" or "license()" for more information.
##>>> ================================ RESTART ================================
##>>> 
##Enter an integer: 8
##2.7178571428571425
##>>> 
