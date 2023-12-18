#Given an array of size N The task is to rotate array by D elements towards right
#Sample Input: arr = [1, 2, 3, 4, 5], D = 2
#Sample Output: arr after rotation = [4, 5, 1, 2, 3]
def reverse_list_up_to_k(arr, k):
   
    arr[:k] = arr[:k][::-1]

   
    arr[k:] = arr[k:][::-1]

   
    arr[:] = arr[::-1]


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k_value = 4

print("Original list:", my_list)


reverse_list_up_to_k(my_list, k_value)

print("Reversed list:", my_list)
