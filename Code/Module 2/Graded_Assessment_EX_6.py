# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:31:22 2020
Complete the body of the format_name function. 
This function receives the first_name and last_name parameters and then returns a properly formatted string.

Specifically:

If both the last_name and the first_name parameters are supplied, the function should return:

"Name: last_name, first_name"

If only one name parameter is supplied (either the first name or the last name) , the function should return:

"Name: name"

Finally, if both names are blank, the function should return the empty string:
@author: Ragib Shahariar Ayon
"""

def format_name(first_name, last_name):
	# code goes here
    if len(first_name)>0 and len(last_name)>0:
        str_to_print= "Name: "+last_name+", "+first_name
        return str_to_print
    elif len(first_name)==0 and len(last_name)>0:
        str_to_print= "Name: " + last_name
        return str_to_print
    elif len(first_name)>0 and len(last_name)==0:
        str_to_print="Name: "+first_name
        return str_to_print
    else:
        str_to_print=''
        return str_to_print

print(format_name("Ernest", "Hemingway"))
# Should be "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should be "Name: Madonna"

print(format_name("Voltaire", ""))
# Should be "Name: Voltaire"

print(format_name("", ""))
# Should be ""