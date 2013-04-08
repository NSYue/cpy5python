# file_name: nirc_validation.py
# author: Nie Shuyue

import re

def check_a(nric):
    weights = [2, 7, 6, 5, 4, 3, 2]
    check_map = {10:'A', 9:'B', 8:'C', 7:'D', 6:'E', 5:'F', 4:'G', 3:'H', 2:'I', 1:'Z', 0:'J'}

    sum_product = 0
    for i in range (1,8):
        sum_product = sum_product +(int(nric[i]) * weights[i-1])
        print(sum_product)
    remainder = sum_product % 11
    print (remainder)
    return check_map[remainder]

def check_b(nric):
    weights = [2, 7, 6, 5, 4, 3, 2]
    check_map = {10:'K', 9:'L', 8:'M', 7:'N', 6:'P', 5:'Q', 4:'R', 3:'T', 2:'U', 1:'W', 0:'X'}

    sum_product = 0
    for i in range (1,8):
        sum_product = sum_product + (int(nric[i]) * weights[i-1])
    sum_product = sum_product + 4
    remainder = sum_product % 11
    return check_map[remainder]

nric = input("Enter a NRIC:")
nric = nric.upper()

if nric[0] == "S":
    if (nric[1:3]<"68") and (nric[1] > "1")and (not check_a(nric) == nric[8]):
        print ("The NRIC is invalid.")
    else:
        print ("The NRIC is valid.")

elif nric[0] == "T":
    if (nric[1:3] < "68") and (nric[1] > "3")and (not check_a(nric) == nric[8]):
        print ("The NRIC is invalid.")
    else:
        print ("The NRIC is valid.")

elif nric[0] == "F":
    if check_b(nric) == nric[8]:
        print ("The NRIC is valid.")
    else:
        print("The NRIC is invalid.")

elif nric[0] == "G":
    if check_b(nric) == nric[8]:
        print ("The NRIC is valid.")
    else:
        print("The NRIC is invalid.")

    
