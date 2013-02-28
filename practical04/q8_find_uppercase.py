# Filename: q8_find_uppercase.py
# Author: Nie Shuyue
# Created: 20130226
# Modified: 20130226
# Description: A recursive function to get the number of uppercase
# letters in a string

# Function
def find_num_uppercase(n):
    if len(n) == 1:
        return int(n[0].isupper())
    else:
        return n[0].isupper() + find_num_uppercase(n[1:])

# main
n = str(input("Enter a string: "))
print ("Number of uppercase letters in the string is", find_num_uppercase(n))


##TEST
##Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
##Type "copyright", "credits" or "license()" for more information.
##>>> ================================ RESTART ================================
##>>> 
##Enter a string: WeLcome
##Number of uppercase letters in the string is 2
##>>> 
