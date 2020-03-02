# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:43:31 2020
The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?
@author: Ragib Shahariar Ayon
"""

def highlight_word(sentence, word):
  return(sentence.replace(word, word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
