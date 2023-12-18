#Write a Python program to calculate the sum of digits of a given number until the sum
#becomes a single-digit number

def dsum(num):
    sum = 0
    if num < 10:
        return num
    
    else:
        while num>0:
         temp = num%10
         sum = sum + temp
         num = num//10
    return dsum(sum)


num = 12345
print(dsum(num))