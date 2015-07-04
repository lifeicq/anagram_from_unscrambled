#!/usr/bin/env python

#This is my ASCII character calculation program that provides a sum of all characters
#Coded by LifeIcq

print "Welcome to ASCII word converter and its sum calculator!"
phrase = raw_input("Please enter your scrambled phrase here for ASCII calculation:")
temp = 0
final_Value = 0

for letter in phrase:
    temp = ord(letter)
    print temp
    final_Value += temp

print final_Value
print "Thank you for using this program!"
