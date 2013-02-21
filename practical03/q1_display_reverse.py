# Filename: q1_display_reverse.py
# Author: Nie Shuyue
# Created: 20130216
# Modified: 20130216
# Description: Program to display an integer in reverse order.

# write the function
def reverse_int(n):
    
    #reverse the integer
    reversenum = n[ : :-1]
    
    # display and get the result
    print ("reverse_int(", n,") = ",reversenum)
    
# main

# prompt and get the integer
n = input("Enter the integer that you want to reverse: ")
reverse_int(n)

