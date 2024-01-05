# '''  Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.'''

str1 = "Emma253 is Data scientist50000 and AI Expert"
str2=str1.split()
new=[]
for i in str2:
        if i.isalpha() == False and i.isdigit() == False :
            new.append(i)
print(new)