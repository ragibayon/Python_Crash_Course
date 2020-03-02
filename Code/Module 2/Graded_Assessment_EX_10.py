# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:32:50 2020
The fractional_part function divides the numerator by the denominator, 
and returns just the fractional part (a number between 0 and 1). 
Complete the body of the function so that it returns the right number. 
Note: Since division by 0 produces an error, if the denominator is 0, 
the function should return 0 instead of attempting the division.
@author: Ragib Shahariar Ayon
"""

def fractional_part(numerator, denominator):
    if numerator==0 or denominator==0:
        return 0
    
    result=numerator % denominator
    
    if result==0:
        return 0
    else:
        return result/denominator

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0