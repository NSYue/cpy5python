# Filename:q7_generate_payroll.py 
# Author: Nie Shuyue
# Date: 20130122
# Modified: 20130122

# main

# prompt and get input
name= input("Enter name: ")
number= int(input("Enter number of hours worded weekly: "))
pay= float(input("Enter hourly pay rate: "))
cpf= input("Enter CPF contribution rate(%): ")

#calculation
gross= pay*number
tcpf= gross*int(cpf)*0.01
net= gross-tcpf

# display result
print ("Payroll statement for ",(name))
print ("Number of hours worked in week: ",(number))
print ("Hourly pay rate: $","{0:.2f}".format(pay))
print ("Gross pay = $","{0:.2f}".format (gross))
print ("CPF contribution at",(cpf),"% = $", "{0:.2f}".format(tcpf))
print ("Net pay = $","{0:.2f}".format(net))
