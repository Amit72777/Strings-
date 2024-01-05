'''Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits that appear in the string,
ignoring all other characters
'''

str = input("Enter the string :")
total = 0
sum = 0
for i in str :
    if i.isdigit() == True : # find digit in string 
        total +=1
        sum+=int(i)
# print  according to condition 
print("the total digit in  string is : ",sum)
print("The average of the digits is ",round(sum/total,2))