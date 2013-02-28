# Filename: q4_print_reverse.py
# Author: Nie Shuyue
# Created: 20130224
# Modified: 20130226
# Description: A recursive function to reverse an integer.

# Function
def reverse_int(n):
    if n//10 == 0:
        return n
    else:
        return (n%10)*10**(len(str(n))-1) + reverse_int(n//10)

# main
n = int(input("Enter an integer: "))
print("The reversed integer is: ",reverse_int(n))


    
##TEST
##Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
##Type "copyright", "credits" or "license()" for more information.
##>>> ================================ RESTART ================================
##>>> 
##Enter an integer: 1234
##The reversed integer is: 4321
##>>> 
