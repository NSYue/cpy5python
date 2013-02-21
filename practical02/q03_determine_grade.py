# Filename:q03_determine_grade.py
# Author: Nie Shuyue
# Date: 20130129
# Modified: 20130129
# Description: Program to determine the grade
# according to the score.

# main

# Prompt and get the score
score=int(input("Enter the score: "))

if 70 <= score <= 100:
    print ("A")

elif 60 <= score <= 69:
    print ("B")

elif 55 <= score <= 59:
    print ("C")

elif 50 <= score <= 54:
    print ("D")

elif 45 <= score <= 49:
    print ("E")

elif 35 <= score <= 44:
    print ("S")

elif 0 <= score <= 35:
    print ("U")

else:
    print ("Invalid! Score must be within 0 - 100.")
