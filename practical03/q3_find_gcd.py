# Filename: q3_find_gcd.py
# Author: Nie Shuyue
# Created: 20130217
# Modified: 20130218
# Description: Program to display the greatest
# common divisor of 2 positive integers

# Function
def gcd(a, b):
    # test the greatest commom divisor
    c = min(a, b)
    while a % c != 0 or b %c !=0:
            c -=1
    # return the result
    return c

# main
print (gcd(24, 16))
print (gcd(255, 25))
