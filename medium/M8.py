#8. Write a Python function that counts the number of vowels in a given string.
#Sample Input: string = "Hello, World!"
#Sample Output: Number of vowels: 3

my_set = {'a','e','i','o','u'}
count = 0
str = "hello,world"
for i in str:
    if i in my_set:
        count = count + 1

print(count)