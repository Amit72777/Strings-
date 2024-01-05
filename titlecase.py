'''Excercise 15 Write a python program to convert a string to title case without using the title()
'''

str1 =input("Enter the string :")
print(str1.title())
str1 = str1[0].upper() +str1[1:]

print(str1)