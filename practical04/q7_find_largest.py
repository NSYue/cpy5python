# Filename: q7_find_largest.py
# Author: Nie Shuyue
# Created: 20130226
# Modified: 20130226
# Description: A recursive funtion that returns the latgest integer in an array

# Function
def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return max(alist[0], find_largest(alist[1: ]))

# main
n= int(input("Enter the number of elements in the list: "))
alist= []
for i in range (0, n):
    a = int(input("Enter the number: "))
    alist.append(a)
print ("The largest among them is: ",find_largest(alist))

##TEST
##Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
##Type "copyright", "credits" or "license()" for more information.
##>>> ================================ RESTART ================================
##>>> 
##Enter the number of elements in the list: 4
##Enter the number: 34
##Enter the number: 5
##Enter the number: 66
##Enter the number: 7
##The largest among them is:  66
##>>> 



