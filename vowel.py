str = input("Enter the sentence :")
new = []
for i in str.lower() :
    if i in "aeiou" and i not in new:
        new.append(i)

print("The Vowel are : ",new )