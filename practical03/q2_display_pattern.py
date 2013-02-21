# Filename: q2_display_pattern.py
# Author: Nie Shuyue
# Created: 20130218
# Modified: 20130218
# Description: Program to display numbers in a pattern

# Function
def display_pattern(n):
    # get the number and spacing in one line
    # when there is no spacing in front
    f = ""
    for i in range (1, n+1):
        f = f +str(i)+" "
    # calculate the spacing
    for i in range (1, n+1):
        if i < 10:
            spacing = i*2
        elif 10<=i<100:
            spacing = 9*2 + (i-9)*3
        elif 100<=i<1000:
            spacing = 9*2 + 90*3 + (i-99)*4
        # display the spacing in front
        print (" "*(len(f)-spacing), end ="")
        # display the number after the spacing
        for x in range (i,0,-1):
            print(x, end=" ")
        print()
    
# main
n= int(input("Display pattern for integer:"))
display_pattern(n)
