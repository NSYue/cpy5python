# Filename: q3_find_gcd.py
# Author: Nie Shuyue
# Created: 20130224
# Modified: 20130224
# Description: Find the greatest common divisor via recursion.

# Function
def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

# main
print ("Greatest common divisor is: ",gcd(24, 16))
print ("Greatest common divisor is: ",gcd(255, 25))



##TEST
##Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
##Type "copyright", "credits" or "license()" for more information.
##>>> ================================ RESTART ================================
##>>> 
##Greatest common divisor is:  8
##Greatest common divisor is:  5
##>>> 
