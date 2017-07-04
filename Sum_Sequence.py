# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 08:19:39 2017

@author: USER
"""

import numpy as np

# Function breaks a range into an int of those numbers
# eg r2i(3, 6) returns the int 3456
def r2i (num1,num2):
    if num1 == num2:
        return num1
    else:
        j = ""
        for i in range(num1, num2+1):
            j += str(i)
        return int(j)

# initialise the list
# values will be a list of tupples. Each tupple is a set of numbers that 
#make the 1 - 10 range    
values = []

x = 6545
# Nested for loops to populate values

#2 numbers
#for i in range (1,9):
#             v1 = r2i(1,i)
#             v2 = r2i(i+1,9)
#             row = (v1, v2)
#             values.append(row)    

#3 numbers
for i in range (1,9):
    for j in range (i+1,9):
             v1 = r2i(1,i)
             v2 = r2i(i+1,j)
             v3 = r2i(j+1,9)        
             #print (str(v1)  + str(v2) +  str(v3) +  str(v4))
             row = (v1, v2, v3)
             values.append(row)

#4 numbers
#for i in range (1,9):
#    for j in range (i+1,9):
#        for k in range (j+1, 9):
#             v1 = r2i(1,i)
#             v2 = r2i(i+1,j)
#             v3 = r2i(j+1,k)
#             v4 = r2i(k+1,9)         
#             #print (str(v1)  + str(v2) +  str(v3) +  str(v4))
#             row = (v1, v2, v3, v4)
#             values.append(row)

#Convert list to array
np_values = np.array(values)
 
# Each number can be added two ways:
# -123 + 456 -789 - this is an example 3 number 3 signs
# 123 + 456 -789 - this is an example of 3 number 2 signs as the plus at the
# start is hidden
signs_2num_2sign = np.array([[1, 1],
         [1, -1],
         [-1, 1],
         [1, 1]])
    
signs_3num_2sign = np.array([[1, 1, 1],
         [1, 1, -1],
         [1, -1, 1],
         [1, 1, 1]])

            
signs_3num_3sign = np.array([[1, 1, 1],
         [1, 1, -1],
         [1, -1, 1],
         [-1, 1, 1],
         [-1, -1, -1],
         [-1, -1, 1],
         [-1, 1, -1],
         [1, -1, -1]])

signs_4num_3sign = np.array([[1, 1, 1, 1],
         [1, 1, 1, -1],
         [1, 1, -1, 1],
         [1, -1, 1, 1],
         [1, -1, -1, -1],
         [1, -1, -1, 1],
         [1, -1, 1, -1],
         [1, 1, -1, -1]])

# update the name of the second for loop here as required    
for i in np_values:
    for j in signs_3num_2sign:
        prod = np.sum(i*j)
        if prod>-300 and prod< 300:
            print (prod)
            print (i)
            print (j)
    



