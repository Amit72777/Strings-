''' Append nedw string n the middle of a given string

Or 
Given two string , s1 and s2 . Write a programm to create a new string s3 appending s2 in the middle of s1 
'''

s1 = input("Enter the first strintg ")
s2 = input("Enter the second string ")
a = len(s1)//2 # find the middle index number of string
s3 = s1[:a] + s2 + s1[a:]

print(" The new string is : ",s3)