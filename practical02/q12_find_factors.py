# Filename: q12_find_factors.py
# Author: Nie Shuyue
# Created: 20130205
# Modified: 20130205
# Description: Program to display all the smallest
# factors of an integer

# main

# prompt and get the integer
num = int(input("Enter an integer: "))
# define factor as a list
factor = []

running = True

# calculate and get the factor list
for i in range (2, num):
    while num % i ==0:
        factor.append (i)
        num /= i

# arrange the output
for i in range (0, len(factor)):
    if running == True:
        print (factor [i], end = "")
        running = False
    else:
        print (",", factor [i], end = "")
