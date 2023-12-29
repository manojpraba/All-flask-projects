#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    grades_round=[]
    for n in grades:
       
        if n>=38:
            if n%5!=0:
                a=n
                for i in range(1,3):
                    
                    n=n+1
                    if n%5==0:
                        grades_round.append(n)
                        break
                else:
                    grades_round.append(a)
                    
            else:
                grades_round.append(n)
        
        else:
            grades_round.append(n)
    
    return grades_round
                        
                    
                
            
                

if __name__ == '__main__':
   
    grades=[73,67,38,33]
    print(gradingStudents(grades))
