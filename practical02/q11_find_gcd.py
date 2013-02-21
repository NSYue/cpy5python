# Filename: q11_find_gcd.py
# Author: Nie Shuyue
# Created: 20130205
# Modified: 20130205
# Description: Program to find the common divisor of two integrs

# main

# prompt and get the two integers
n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))

running = True
# get the minimum of n1 and n2
if n1 < n2 :
    # calculate the commom divisor
    for i in range (n1, 0, -1):
        if n1 % i ==0 and n2 % i ==0 and running == True:
             # display the result
            print ("Largest commom divisor: ", i)
            running = False
    
# calculate the commom divisor
else :
    for i in range (n2, 0, -1):
        if n1 % i ==0 and n2 % i ==0 and running == True:
    # display the result
            print ("Largest common divisor: ", i)
            running = False
