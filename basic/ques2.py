#2. Write a program that accepts a string as an input from the user and calculate the
#number of digits and letters.
#Hello123
#Alph -> 5 and number -> 3
str = input()
alphanumeric_count = 0
letter_count = 0
for char in str:
    if char.isnumeric():
        alphanumeric_count+=1
    if char.isalpha():
        letter_count+=1
res1 = f"Letter-->:{letter_count} " 
res2 = f"Alpha-->:{alphanumeric_count}" 
print(res1+res2)