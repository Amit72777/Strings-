''' String Characters Balance Test

Write a program to check if two strings are balanced. For exaple, strings s1 ans s2 are balanaced if all the characters
in the  s1 are present in s2 . 
The character's postion doesn't matter.

'''
str1 = input("Enter the 1st string:")
str2 = input("Enter the 2nd string :")
count = 0 
for i in str1:

    if i in str2 :
        count+=1

if count == len(str1):
    print("s1 and s2 are balnace")
else :
    print("s1 and s2 are not balance ")