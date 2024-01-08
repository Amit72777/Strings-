'''
Create a mixed String using the following rules
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the
last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at
the end of the result.
Not:- Both input string is equal 

'''

str1,str2 = input("Enter the both string using (,) for seperate ").split(",")
str3=""
print(str1,str2)

for  i,j in  zip(str1,str2[::-1]):
    str3 = str3 + i+j

print(str3)