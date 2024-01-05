''' Replace each special symbol with # in the following string
str1 = '/*Jon is @developer & musician!!'
Expected-->##Jon is #developer # musician##'''


str = input("Enter the string :")
s = ''
for i in str :
    if i.isdigit() == True or i.isalpha() == True or i == ' ' :
        s += i 
    else : 
        i = '#'
        s+=i
print(s)