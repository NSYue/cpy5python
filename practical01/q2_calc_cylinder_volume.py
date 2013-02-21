# Filename:q2_calc_cylinder_volume.py
# Author: Nie Shuyue
# Date: 20130122
# Modified: 20130122
# Description: Program to get the radius and length
# of a cylinder and computes its volume

#main

#prompt and get radius
radius = float(input("Enter radius in cm: "))

#prompt and get the length
length = float(input("Enter length in cm: "))

#calculate the area
import math
area = radius * radius * math.pi

#calculate the volume
volume = area * length

#display result
print ("Volume of the sylinder = {0:.2f}".format (volume))
