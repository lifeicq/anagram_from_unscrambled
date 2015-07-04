#!/usr/bin/env python

#Welcome to Reverser.Py 
word = raw_input("What is the word to be reversed?")
word = word.replace(" ", "")
new_word = word[::-1] #I pick my string up flip it and reverse it!
new_word = new_word[-1:] + new_word[:1] + new_word[1:-1] #Fancy string slicing.
print new_word
print "<usage> python reverser.py <word>"
