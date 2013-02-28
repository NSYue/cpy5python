# Filename: q5_count_letter.py
# Author: Nie Shuyue
# Created: 20130226
# Modified: 20130226
# Description: A recursive function to find out the number of
# occurrence of a specified letter in a string.

# Function
def count_letter(stri, ch):
    if len(stri)==1:
        return stri[0]==ch
    else:
        return (stri[0]==ch) + count_letter(stri[1:], ch)

# main
stri = str(input("Enter a word: "))
ch = str(input("Enter the letter in the word: "))
print ("Number of occurance of it is: ",count_letter(stri, ch))


##TEST
##>>> ================================ RESTART ================================
##>>> 
##Enter a word: good
##Enter the letter in the word: o
##Number of occurance of it is:  2
##>>> 
