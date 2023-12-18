#3. Given an array of N integers, and an integer K, find the number of pairs of elements
#in the array whose sum is equal to K.
#Sample Input: arr = [1, 2, 3, 4, 5], k = 6
#Sample Output: Pair count: 2
arr = [1, 2, 3, 4, 5]
k = 6
count =0
s = len(arr)
for i in range(s):
    sum = k - arr[i]
    
    for j in range(i+1,s):
        if arr[j]==sum:
            count = count + 1

print(count)


##optimized
arr = [1, 2, 3, 4, 5]
k = 6
count = 0
seen_numbers = set()

for num in arr:
    complement = k - num
    if complement in seen_numbers:
        count += 1
    seen_numbers.add(num)

print(count)

