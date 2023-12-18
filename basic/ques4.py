#Write a Python program to find the sum of all odd numbers between two given
#numbers.
#Start = 1, stop = 10
#Sum of odd numbers: 25

num1 = int(input())
num2 = int(input())

i = num1
sum =0
for i in range(num2):
    if i%2!=0:
        sum = sum+i
print(sum)