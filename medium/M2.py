#2. Create a function that takes a list and returns a new list with unique elements of the
#first list.
#Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
#Sample Output: list2 = [1, 2, 3, 4, 5]


list1 = [1, 2, 2, 3, 4, 4, 5, 5]
list2 = set(list1)
list3 = list(list2)
print(list3)
