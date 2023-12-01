# name = input("Enter your name :")
# age  = input ("Enter your age :")  Normal form
name,age = input("Enter your name and age ").split()
print(name)
print(age)
print("your name is " + name + "& age is " + age )
print("Your name is : {} & age is {}".format(name,age))
print(f" YOur name  is : {name} & age is :{age}") # python 3.6 style
