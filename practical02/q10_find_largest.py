# Filename: q10_find_largest.py
# Author: Nie Shuyue
# Created: 20130205
# Modified: 20130205
# Description: Program to find the largest integer
# for n*n*n less than 12000

# main

# define n
n = 0

# calculate the smallest integer of n
# for which n*n*n >12000
while (n*n*n < 12000):
    n += 1
# get the largest integer for n*n*n <12000
n = n - 1

# display the result
print (n)
