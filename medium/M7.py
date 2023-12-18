#Write a Python function that finds the median of a list of numbers.
#Sample Input: number_list = [7, 2, 5, 1, 9, 3]
#Sample Output: Median: 4.5
l1 = [7, 2, 5, 1, 9, 3]
l1.sort()
if len(l1)%2!=0:
    median = l1[len(l1)//2]

else:
    median = (l1[len(l1)//2] + l1[len(l1)//2 - 1])/2
print(median)

