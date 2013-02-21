# Filename: q7_display_matrix.py
# Author: Nie Shuyue
# Created: 20130221
# Modified: 20130221
# Description: Program to display a n by n matrix
# with random element of 0 or 1

# Function
def print_matrix(n):
    import random
    for i in range(0, n):
        for j in range(0, n):
            print(random.randint(0,1), end=" ")
        print()

# main
n = int(input("Enter the number of lines in matrix: "))
print_matrix(n)
