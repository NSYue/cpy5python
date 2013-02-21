# Filename: q4_sum_series.py
# Author: Nie Shuyue
# Created: 20130218
# Modified: 20130218
# Description: Program to calculate a series.

# Function
def m_series(i):
    # get the title
    print ("i         m(i)")
    # get first number
    print ("1         0.5000")
    y = [0 for i in range (0, i+1)]
    y[1] = 0.5
    # calculate the following numbers
    for i in range (2, i+1):
        y[i] = y[i-1] + i/(i+1)
        num = i
        print ("{0:<9}".format(num), "{0:.4f}".format(y[i]))

# main
x = int(20)
m_series (x)
