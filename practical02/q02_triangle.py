# Filename:q02_triangle.py
# Author: Nie Shuyue
# Date: 20130129
# Modified: 20130129
# Description: Program to identify a triangle
# and calculate its perimeter.

# main

# Prompt and get the length of each
# side of the triangle
a = int(input("Enter side 1:"))
b = int(input("Enter side 2:"))
c = int(input("Enter side 3:"))

# identify the triangle
if a + b > c and a + c > b and b + c > a:
    d = a + b + c
    
    # display the reslut
    print("Perimeter = ", d)
else:
    print("Invalid triangle!")
