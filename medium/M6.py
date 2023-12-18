#6. Write a Python program to check if a number is a power of two using recursion.

def pow2(num):
    if num == 1:
        print("Power of two")

    elif num%2!=0:
        print("Not power of two")

    else:
        num = num//2
        pow2(num)

num = 16
pow2(num)