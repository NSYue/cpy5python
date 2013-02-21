# Filename: q08_top2_scores.py
# Author: Nie Shuyue
# Created: 20130204
# Modified: 20130205
# Description: Program to get the top 2 scores of a group of students

# main

# prompt and get the number of students
num = int(input("Enter the number of students: "))

# define top, second score and the names
top = -10000
sec = -10000
ntop = ""
nsec = ""

# get the name and the score
for i in range (0, num):
    name = input("Enter the name of the student: ")
    score = int (input("Enter the score of the student: "))
    # process and find out the top and second scores
    if score > top:
        sec = top
        nsec = ntop
        top = score
        ntop = name
    elif score > sec:
        sec = score
        nsec = name

# display the results
print("Highest scorer is: ", ntop)
print("Highest score is: ",top)
print("Second highest scorer is :", nsec)
print("Second highest score is: ",sec)
