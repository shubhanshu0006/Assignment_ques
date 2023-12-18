#Write a Python program to reverse a number using a while loop.
#Sample Input: num = 12345
#Sample Output: revnum = 54321

num = int(input())
rev_num = 0
temp = 1
temp = num
while num>0:
            temp = num%10
            rev_num = rev_num*10 + temp
            num = num//10

print(rev_num)
