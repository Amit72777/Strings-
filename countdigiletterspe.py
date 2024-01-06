''' 
Count all letters , digits and special symbols form a given string 
'''
str = input("Enter the string :")
count_char=0
count_digit= 0
count_special_symbol=0

for i in str:
    if i.isdigit() == True:
        count_digit+=1
    elif i.isalpha() == True:
        count_char+=1
    else :
        count_special_symbol+=1


print(f" the Charater is {count_char} \n the digit is = {count_digit} \n the special symbol is {count_special_symbol}" )