# Write a Python program to check if a given number is a perfect number.


num= int(input())

sum = 0
for i in range(1,num):
    if num%i==0:
        sum+=i


if sum==num:
    print("perfect number")