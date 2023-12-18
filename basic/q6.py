#7. Write a Python program to check if a string is an anagram of another string.
#string1 = "listen", string2 = "silent"
#Output: True
s1 = input()
s2 = input()

r1 = sorted(s1)
r2 = sorted(s2)
if r1==r2:
    print("Anagram")
