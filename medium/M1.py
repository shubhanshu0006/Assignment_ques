#1. Write a Python program to find the common elements between two lists.
#Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
#Sample output: [4, 5]

l1 = [1,2,3,4,5]
l2 = [4, 5, 6, 7, 8]
l3 = []



l1.sort()
l2.sort()
i =0
j =0
k = 0
while i<len(l1) and j <len(l2):
    if l1[i] == l2[j]:
        l3.insert(k,l1[i])
        i = i + 1
        j = j + 1
        k = k + 1

    elif l1[i] > l2[j]:
        j= j + 1

    else:
        i= i + 1

print(l3)
