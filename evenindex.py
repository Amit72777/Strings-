''' 
print the character from a string that aea present at an even index number 
            Or 
Write a programm to accept a string from the user and display characters that are present at an even index number 
'''
str = input("Enter the string :")
s=[]
s.extend(str[::2])
print(s) # split function for seperate the element 
