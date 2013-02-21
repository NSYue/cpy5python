# Filename: q5_compute_series.py
# Author: Nie Shuyue
# Created: 20130218
# Modified: 20130218
# Description: compute a series.

# Function
def series(i):
    # check the number
    if i % 2 == 0:
        print ("You should enter an odd number!")
    else:
        print ("i    m(i)")
        sum = 0.0
        a = 1
        while a <= i:
            sum = sum + float(1/(2*a-1))
            sum = sum - float(1/(2*a+1))
            print ("{0:<4}".format(a), "{0:.11f}".format(sum * 4))
            a +=2

# main
i = int(input("Enter an odd number: "))
series(i)
