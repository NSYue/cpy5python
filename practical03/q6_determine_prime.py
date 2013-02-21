# Filename: q6_determine_prime.py
# Author: Nie Shuyue
# Created: 20130220
# Modified: 20130220
# Description: Program to display the first 1000
# prime numbers in a certain format.

# Function
def is_prime(n):
    import math
    for i in range (2, int(math.sqrt(n))+1):
        if (n %i ==0):
            return False
    else:
        return True
    
# main
n = 2
total = 0
# get the format
while total <1000:
    if is_prime(n):
        total += 1
        print("{0:<6d}".format(n), end = "")
        # change line when there are 10 numbers
        if total % 10 == 0:
            print()
    n += 1
        



        
