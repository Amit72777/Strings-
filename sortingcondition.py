'''
Arrange string characters such that lowercase letters should come first
'''
str = input("Enter the string ")
a = [] 
a.extend(str) # add  string alphabate in list 


a.sort() # sorting function can change in order of item in list 
a.reverse() # small letter in !st plat and capital letter in back side 

s1 = "".join(a)  # convert list into a string 
print(s1)